#!/usr/bin/env python3
"""
Pull Outlook calendar and draft weekly priorities email.
Scheduled to run daily at 9:30 AM via Windows Task Scheduler.
"""

import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

try:
    import win32com.client
except ImportError:
    print("ERROR: win32com not installed. Run: pip install pywin32")
    sys.exit(1)


def get_outlook_calendar_events(days_ahead=7):
    """Fetch upcoming events from Outlook calendar for the next N days."""
    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")
        calendar_folder = namespace.GetDefaultFolder(9)  # 9 = olFolderCalendar
        
        # Get events for the next N days
        start_date = datetime.now()
        end_date = start_date + timedelta(days=days_ahead)
        
        items = calendar_folder.Items
        items.Sort("[Start]")
        items.IncludeRecurrences = True
        
        # Filter by date range
        restriction = f"[Start] >= '{start_date.strftime('%m/%d/%Y')}' AND [Start] < '{end_date.strftime('%m/%d/%Y')}'"
        restricted_items = items.Restrict(restriction)
        
        events = []
        for item in restricted_items:
            try:
                event = {
                    "subject": item.Subject,
                    "start": item.Start.strftime("%A, %B %d at %I:%M %p"),
                    "duration_minutes": item.Duration,
                    "location": item.Location or "Not specified",
                    "categories": item.Categories or "Uncategorized"
                }
                events.append(event)
            except Exception as e:
                print(f"Warning: Could not process event: {e}")
                continue
        
        return events
    
    except Exception as e:
        print(f"ERROR: Could not access Outlook: {e}")
        return []


def draft_weekly_priorities_email(events):
    """Generate email body with weekly priorities based on calendar."""
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())  # Monday of this week
    week_end = week_start + timedelta(days=6)
    
    email_body = f"""Subject: Weekly Priorities - {week_start.strftime('%B %d')} to {week_end.strftime('%B %d, %Y')}

Dear Team,

Below is a summary of my key priorities and scheduled commitments for the week of {week_start.strftime('%B %d, %Y')}:

UPCOMING CALENDAR EVENTS ({len(events)} items):
"""
    
    if events:
        for i, event in enumerate(events, 1):
            email_body += f"\n{i}. {event['subject']}"
            email_body += f"\n   When: {event['start']}"
            email_body += f"\n   Duration: {event['duration_minutes']} minutes"
            if event['location'] != "Not specified":
                email_body += f"\n   Location: {event['location']}"
            email_body += "\n"
    else:
        email_body += "\n(No calendar events scheduled)\n"
    
    email_body += """
KEY FOCUS AREAS:
- [Add your priorities here]
- [Add blockers/risks here]
- [Add dependencies here]

AVAILABILITY:
- [Note any time blocks or constraints]

Please let me know if you have questions or need to sync.

Best regards,
Krishna Siram
"""
    
    return email_body


def save_draft_email(email_body):
    """Save email as draft in Outlook or as text file."""
    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)  # 0 = olMailItem
        
        mail.Subject = email_body.split('\n')[0].replace("Subject: ", "")
        mail.Body = email_body
        mail.Save()  # Saves to Drafts folder
        
        print(f"✓ Email draft saved to Outlook Drafts at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    
    except Exception as e:
        print(f"Warning: Could not save to Outlook Drafts ({e}). Saving to file instead...")
        
        # Fallback: save to text file
        try:
            draft_dir = Path.home() / "Desktop" / "Email Drafts"
            draft_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            draft_file = draft_dir / f"weekly_priorities_{timestamp}.txt"
            
            with open(draft_file, 'w') as f:
                f.write(email_body)
            
            print(f"✓ Email draft saved to {draft_file}")
            return True
        
        except Exception as e2:
            print(f"ERROR: Could not save draft: {e2}")
            return False


def main():
    """Main workflow: pull calendar → draft email."""
    print(f"\n{'='*60}")
    print(f"Weekly Priorities Email Generator")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Step 1: Fetch calendar events
    print("📅 Pulling Outlook calendar events...")
    events = get_outlook_calendar_events(days_ahead=7)
    print(f"   Found {len(events)} events for the next 7 days")
    
    # Step 2: Draft email
    print("✉️  Drafting weekly priorities email...")
    email_body = draft_weekly_priorities_email(events)
    
    # Step 3: Save draft
    print("💾 Saving email draft...")
    success = save_draft_email(email_body)
    
    if success:
        print("\n✓ Process completed successfully!")
    else:
        print("\n✗ Process completed with errors")
        sys.exit(1)


if __name__ == "__main__":
    main()
