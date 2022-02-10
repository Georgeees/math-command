import random
import asyncio
from nextcord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.command()
async def math(ctx):
		# The range of numbers that the riddle will provide (Can be changed)
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    result = float(num_1) + float(num_2) # The results of the first random number with the second random number

    def check_correct(message):
        return message.author == ctx.author and message.content.isdigit()
				# Checks that the answer is a number

    e = nextcord.Embed(
        title= 'Math Riddle :brain:',
        description= f'Riddle: **{num_1}**+**{num_2}**',
        color= nextcord.Colour.random() # The embed that will be sent to provide the riddle. Can be customzied
    )
    await ctx.send(embed=e)

    try:
        guess = await bot.wait_for('message', check=check_correct, timeout=10) # Wait for the author's answer. You can also set whatever timeout you want!
    except asyncio.TimeoutError:
        return await ctx.send(f'You ran out of time! The answer was: **{result}**') # Timeout error
    if int(guess.content) == result:
        await ctx.send('You are correct! Congratulations!') # If the answer is correct, the following will be sent
    else:
        await ctx.send(f'Wrong answer. The correct answer was: {result}.') # If the answer is wrong, the following will be sent

bot.run('token')
