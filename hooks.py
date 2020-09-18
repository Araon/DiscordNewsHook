from dhooks import Webhook, Embed
from inshorts import getNews
import json
import time

urlLole = "https://discord.com/api/webhooks/756417999971287071/ZXrh-fJIpapJlDg2wjv4RZvDbh-9QReINIhKK5frjB3MmsjLfql-N1AIym9fTiNxCcwP"

#testUrl = "https://discord.com/api/webhooks/756397412784013402/pg6hyvthWE8-U1zyu3v3Hv1evbx8r36VMajXi3MpZK8Hlb-Uw5PmgEVSuvI0IUKuz7m-"

hook = Webhook(urlLole)

newz = getNews("")

hook.send('**Daily Briefing**')

for bits in newz['data']:
	newsTitle = bits['title']
	newsContent = bits['content']
	imageUrl = bits['imageUrl']
	newsAuthor = bits['author']
	newsReadmore = bits['readMoreUrl']

	embed = Embed(
	title=newsTitle,
	url=newsReadmore,
	description=newsContent,
	color=0x5CDBF0,
	timestamp='now'
	)
	image1 = imageUrl
	embed.set_image(image1)
	embed.set_footer(text=newsAuthor)


	hook.send(embed=embed)
	time.sleep(2)

hook.send('**Daily News at 8am and 8pm**')


