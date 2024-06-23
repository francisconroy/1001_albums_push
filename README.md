# 1001 albums generator push notifications
After stumbling upon the 1001 albums generator https://1001albumsgenerator.com/
I thought it would be fun to create a push notification service that would send 
today's album to my phone every day.

The current implementation uses the ntfy.sh service to receive the notifications.
The notification which appears can be "clicked" on the phone which will auto launch the configured streaming services app.

Future plans:
- support for other music platforms supported by 1001 albums project e.g. Apple Music, youtube, deezer, tidal, etc.
- support for multiple projects, perhaps even a configuration UI
- OR integration into the original project
- Support for group mode

## How it works
Simply this app does the following:
- Pulls down the 1001_albums_generator API which contains the metadata for today's album
- Prepares the spofity app link for the notification
- Sends the notification to the ntfy.sh service

## How to configure
Just modify the conf/config.toml with your desired configuration.
Each of the settings are explained within the config file itself.
