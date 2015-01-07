slackfred
=========

![](http://i.imgur.com/Vy78c78.gif)

Alfred workflow to interact, and perform various functions with the service [Slack](http://slack.com/).

## Getting started
1. Install slackfred by visiting the download page in Github or via the [Packal page](http://www.packal.org/workflow/slackfred)
2. Open alfred and type `slt`, then hold `cmd` (apple key) and press `enter`. This will open up the Slack API page. Then look for your team (make sure you're logged in) near the bottom and copy your token.
3. Open alfred and type `slt`, then paste your token and press `enter`.
4. Try one of the commands below!

## Currently Available Functionality
* `slt`: Set your API Token
  * Open alfred and type `slt`, then paste your token. If you don't have a token, then hold `cmd` to open the API page to get one (look for your team near the bottom of the page).
* `slf`: Search files
  * Open alfred and type `slf` to search files. Selecting a file opens it in your browser
* `slk`: Search users and rooms
  * Open alfred and type `slk` to search user and room names. Hitting enter triggers an Applescript to interact with the **desktop** application and passes the selected name. Similar to cmd+k
* `slp`: Set your presence
  * Open alfred and type `slp active` or `slp away`
* `slc`: View, leave and join channels
  * Open alfred and type `slc` to display a searchable list of channels. Selecting a channel with `alt` leaves and `ctrl` lets you join.
* `slclear`: Clear unread messages

## To-do
* Search direct messages
* Create a smoother API key/token process

This workflow was created with the help of [Dean Jackson's](https://github.com/deanishe/alfred-workflow) Alfred  library.
