await client.start_workflow(
    "WeeklySummaryWorkflow",
    "user123",
    id="weekly-summary-user123",
    task_queue="onboarding-assistant",
    cron_schedule="0 9 * * 1"  # Every Monday at 9 AM
)
