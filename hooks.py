from dhooks import Webhook, Embed
import json
import time

hook = Webhook("https://discord.com/api/webhooks/756417999971287071/ZXrh-fJIpapJlDg2wjv4RZvDbh-9QReINIhKK5frjB3MmsjLfql-N1AIym9fTiNxCcwP")



with open('data.json', 'r') as fp:
    newz = json.load(fp)




for bits in newz['data']:
	newsTitle = bits['title']
	newsContent = bits['content']
	imageUrl = bits['imageUrl']
	newsTime = bits['time']
	newsDate = bits['date']
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

hook.send('**Daily News at 8am**')


