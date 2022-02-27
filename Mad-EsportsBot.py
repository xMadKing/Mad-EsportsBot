import discord
import leaguepedia_parser
from discord.ext import commands
import openapi_client
from openapi_client import apis
from openapi_client import models

apiclient = openapi_client.ApiClient(header_name="x-api-key", header_value="0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z")
teams_api = apis.TeamsApi(apiclient)
leagues_api = apis.LeaguesApi(apiclient)
events_api = apis.EventsApi(apiclient)
leagues: models = leagues_api.get_leagues(hl="en-US")
standings = leagues_api.get_standings(hl="en-US", tournament_id=[107417059262120466])
schedule = events_api.get_schedule(hl="en-US", league_id=[98767991302996019])
tony = leagues_api.get_tournaments_for_league(hl="en-US", league_id=98767991299243165)

activity: discord.Activity = discord.Game(name='Penis gang')
status: discord.Status = discord.Status.idle
bot = commands.Bot(command_prefix='$', description="test bot", intents=discord.Intents.default(), activity=activity,
                   status=status)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
#Just a command to check if the bot is online.
async def test(ctx: commands.Context):
    await ctx.send("working")

@bot.command()
#Gets all the live broadcasts on lol-esports.
async def livebroadcasts(ctx: commands.Context):
    live = events_api.get_live(hl="en-US")
    live_leagues = []
    for league in live['data']['schedule']['events']:
        live_leagues.append(league['league']['name'])
    embed_msg = discord.Embed(title="LIVE  🔴", description="Current live broadcasts, see "
                                             + "https://lolesports.com/schedule to watch!")
    embed_msg.set_thumbnail(url='https://logos-world.net/wp-content/uploads/2021/09/LoL-Esports-New-Logo-700x394.png')
    embed_msg.set_footer(text="Powered by Penis Gang™",
                         icon_url="https://i.pinimg.com/originals/ed/f0/53/edf053732edf63388f3af24d4da2e547.jpg")
    for league in live_leagues:
        embed_msg.add_field(name=league, value="More information about the " + league + ": https://lol.fandom.com/wiki/"
                                               + league, inline=False)
    await ctx.send(embed=embed_msg)

@bot.command()
async def LECstandings(ctx: commands.Context):
    standings_raw = leagues_api.get_standings(hl="en-US", tournament_id=[107417059262120466])
    standings = standings_raw['data']['standings'][0]['stages'][0]['sections'][0]['rankings']
    embed_msg = discord.Embed(title='LEC standings', description="Standings of the League of legends European Championship")
    for standing in standings:
        teams_str = ''
        teams = standing['teams']
        for team in teams:
            teams_str += team['code'] + ', '
        teams_str = teams_str[:-2]
        embed_msg.add_field(name=standing['ordinal'],  value=teams_str, inline=False)
    embed_msg.set_thumbnail(url='http://static.lolesports.com/leagues/1592516184297_LEC-01-FullonDark.png')
    embed_msg.set_footer(text="Powered by Penis Gang™",
                         icon_url="https://i.pinimg.com/originals/ed/f0/53/edf053732edf63388f3af24d4da2e547.jpg")
    await ctx.send(embed=embed_msg)

@bot.command()
async def LCKstandings(ctx: commands.Context):
    standings_raw = leagues_api.get_standings(hl="en-US", tournament_id=[107418445247362001])
    standings = standings_raw['data']['standings'][0]['stages'][0]['sections'][0]['rankings']
    embed_msg = discord.Embed(title='LCK standings', description="Standings of the League of legends Korean Championship")
    for standing in standings:
        teams_str = ''
        teams = standing['teams']
        for team in teams:
            teams_str += team['code'] + ', '
        teams_str = teams_str[:-2]
        embed_msg.add_field(name=standing['ordinal'],  value=teams_str, inline=False)
    embed_msg.set_thumbnail(url='http://static.lolesports.com/leagues/lck-color-on-black.png')
    embed_msg.set_footer(text="Powered by Penis Gang™",
                         icon_url="https://i.pinimg.com/originals/ed/f0/53/edf053732edf63388f3af24d4da2e547.jpg")
    await ctx.send(embed=embed_msg)

@bot.command()
async def LPLstandings(ctx: commands.Context):
    standings_raw = leagues_api.get_standings(hl="en-US", tournament_id=[107417779630700437])
    standings = standings_raw['data']['standings'][0]['stages'][0]['sections'][0]['rankings']
    embed_msg = discord.Embed(title='LPL standings', description="Standings of the League of legends Pro League in China")
    for standing in standings:
        teams_str = ''
        teams = standing['teams']
        for team in teams:
            teams_str += team['code'] + ', '
        teams_str = teams_str[:-2]
        embed_msg.add_field(name=standing['ordinal'],  value=teams_str, inline=False)
    embed_msg.set_thumbnail(url='http://static.lolesports.com/leagues/1592516115322_LPL-01-FullonDark.png')
    embed_msg.set_footer(text="Powered by Penis Gang™",
                         icon_url="https://i.pinimg.com/originals/ed/f0/53/edf053732edf63388f3af24d4da2e547.jpg")
    await ctx.send(embed=embed_msg)

@bot.command()
async def LCSstandings(ctx: commands.Context):
    standings_raw = leagues_api.get_standings(hl="en-US", tournament_id=[107458367237283414])
    standings = standings_raw['data']['standings'][0]['stages'][0]['sections'][0]['rankings']
    embed_msg = discord.Embed(title='LCS standings', description="Standings of the League of legends Championship in North America")
    for standing in standings:
        teams_str = ''
        teams = standing['teams']
        for team in teams:
            teams_str += team['code'] + ', '
        teams_str = teams_str[:-2]
        embed_msg.add_field(name=standing['ordinal'],  value=teams_str, inline=False)
    embed_msg.set_thumbnail(url='http://static.lolesports.com/leagues/LCSNew-01-FullonDark.png')
    embed_msg.set_footer(text="Powered by Penis Gang™",
                         icon_url="https://i.pinimg.com/originals/ed/f0/53/edf053732edf63388f3af24d4da2e547.jpg")
    await ctx.send(embed=embed_msg)

bot.run('NjgxNDk0MDg1Mjg2MTAxMDA1.XlPQ0w.CrKA1b3muPpoNEgx4Pd468HdRD4')
