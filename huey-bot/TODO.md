# Huey — Discord Bot TODO

A running list of planned features and systems for Huey, the Valheim server steward.

## 1. Core Discord Interaction
- [ ] Give Huey the ability to read messages in the Discord server.
- [ ] Implement slash commands for interacting with the bot.
- [ ] Add structured logging for all bot actions.

## 2. Server Control (Local or Cloud)
- [ ] Start and stop the Valheim server using instance details from `.env`.
- [ ] Add status checks to confirm whether the server is online.
- [ ] Add safety checks to prevent duplicate start/stop requests.

## 3. Privilege System (All-Father, Valkyrie, Unworthy)
- [ ] Implement a privilege decision tree:
      - All-Father → full permissions
      - Valkyrie → limited permissions (start server)
      - Unworthy → no permissions, receives humorous responses
- [ ] Create a `privileges.json` file to store Discord user IDs and their roles.
- [ ] Add tailored responses based on privilege level.
- [ ] Allow All-Father to assign and revoke roles via Discord commands.

## 4. Game Log Monitoring
- [ ] Parse Valheim server logs to track player uptime.
- [ ] Track when players join/leave.
- [ ] Store player activity history for later analysis.

## 5. Auto-Shutdown Logic
- [ ] Monitor player count in real time.
- [ ] If no players are online for X minutes, initiate safe shutdown.
- [ ] Notify All-Father before shutdown occurs.

## 6. Cost Analysis & Cloud Integration
- [ ] Track CPU and RAM usage to determine ideal instance size.
- [ ] Compare AWS instance costs and estimate monthly usage.
- [ ] Before launching a cloud instance:
      - If cost exceeds threshold → ask All-Father for approval.
      - If cost exceeds hard limit → notify Discord that cloud launch is blocked.
- [ ] Provide fallback instructions for launching a local instance.



