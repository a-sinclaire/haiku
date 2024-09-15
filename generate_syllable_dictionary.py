import json

#  http://www.delphiforfun.org/programs/Syllables.htm
with open('Syllables.txt', encoding='utf-16') as f:
    lines = f.readlines()

syllables_dict = {}

for line in lines:
    try:
        word = line.split('=')[0]
        pronunciation = line.split('=')[1]
        num_syllables = len(pronunciation.split('�'))

        syllables_dict[word] = num_syllables
    except:
        print(line)

with open('SyllablesUpdate.txt') as f:
    lines = f.readlines()

for line in lines:
    try:
        word = line.split('=')[0]
        pronunciation = line.split('=')[1]
        num_syllables = len(pronunciation.split(' '))

        syllables_dict[word] = num_syllables
    except:
        print('2', line)

syllables_dict['unresolve'] = 3
syllables_dict['ozymandias'] = 5
syllables_dict['doomscrolling'] = 3
syllables_dict['reechoes'] = 3
syllables_dict['cucks'] = 1
syllables_dict['uncurls'] = 2
syllables_dict['spectres'] = 2
syllables_dict["'cos"] = 1
syllables_dict['slumbers'] = 2
syllables_dict['mandelbrot'] = 3
syllables_dict['reddit'] = 2
syllables_dict['classist'] = 2
syllables_dict['colour'] = 2
syllables_dict['wavers'] = 2
syllables_dict['fulfil'] = 2
syllables_dict['dewdrops'] = 2
syllables_dict['spliff'] = 1
syllables_dict['bestfriend'] = 2
syllables_dict['throbs'] = 1
syllables_dict['colourful'] = 3
syllables_dict["haiku's"] = 2
syllables_dict['upvotes'] = 2
syllables_dict['pitter'] = 2
syllables_dict['pattering'] = 3
syllables_dict['skyes'] = 1
syllables_dict['cuz'] = 1
syllables_dict['flairs'] = 1
syllables_dict["changin'"] = 2
syllables_dict['bleaches'] = 2
syllables_dict['glistens'] = 2
syllables_dict['molts'] = 1
syllables_dict['meaninglessness'] = 4
syllables_dict['sews'] = 1
syllables_dict['gingers'] = 2
syllables_dict['anagrams'] = 3
syllables_dict['highchair'] = 2
syllables_dict['prouds'] = 1
syllables_dict['rustled'] = 2
syllables_dict['livin'] = 2
syllables_dict['bobbypins'] = 3
syllables_dict['unicorns'] = 3
syllables_dict['contrails'] = 2
syllables_dict['mayhaps'] = 2
syllables_dict["freakin'"] = 2
syllables_dict['featherlight'] = 3
syllables_dict["twilight's"] = 2
syllables_dict['kitties'] = 2
syllables_dict['koi'] = 1
syllables_dict['eunuchs'] = 2
syllables_dict['petrichor'] = 3
syllables_dict["spider's"] = 2
syllables_dict['darks'] = 1
syllables_dict['google'] = 2
syllables_dict['sickeningly'] = 4
syllables_dict['backstreets'] = 2
syllables_dict['guac'] = 1
syllables_dict['snuggles'] = 2
syllables_dict['flavour'] = 2
syllables_dict['aww'] = 1
syllables_dict['quivers'] = 2
syllables_dict['coronavirus'] = 5
syllables_dict['hummus'] = 2
syllables_dict['bleachy'] = 2
syllables_dict['texted'] = 2
syllables_dict["web's"] = 1
syllables_dict["grasshopper's"] = 3
syllables_dict['koda'] = 2
syllables_dict['disarono'] = 4
syllables_dict["paltrow's"] = 2
syllables_dict['steeps'] = 1
syllables_dict['mayhap'] = 2
syllables_dict['knacker'] = 2
syllables_dict['var'] = 1
syllables_dict["bang's"] = 1
syllables_dict['covid'] = 2
syllables_dict['enfolds'] = 2
syllables_dict['barista'] = 3
syllables_dict['fizzing'] = 2
syllables_dict['twink'] = 1
syllables_dict["melody's"] = 3
syllables_dict['snowdrops'] = 2
syllables_dict['illuminati'] = 5
syllables_dict["owl's"] = 2
syllables_dict["arn't"] = 1
syllables_dict['mindfulness'] = 3
syllables_dict['kneels'] = 5
syllables_dict['teardrops'] = 2
syllables_dict['shitposting'] = 3
syllables_dict['chillin'] = 2
syllables_dict['dragonflies'] = 3
syllables_dict['sandcastles'] = 3
syllables_dict['powerpoint'] = 3
syllables_dict['netflix'] = 2
syllables_dict['beaks'] = 1
syllables_dict['hoodied'] = 2
syllables_dict['moar'] = 1
syllables_dict['scatters'] = 2
syllables_dict['sudoku'] = 3
syllables_dict['tetris'] = 2
syllables_dict['mediates'] = 3
syllables_dict["let'em"] = 2
syllables_dict['crashy'] = 2
syllables_dict['trouts'] = 2
syllables_dict["heater's"] = 2
syllables_dict['bindless'] = 2
syllables_dict['roughrider'] = 3
syllables_dict['toasty'] = 2
syllables_dict['colours'] = 2
syllables_dict["ink'd"] = 2
syllables_dict['biblically'] = 3
syllables_dict['ribboned'] = 2
syllables_dict['watercolor'] = 4
syllables_dict['googled'] = 2
syllables_dict['blogging'] = 2
syllables_dict['thuds'] = 1
syllables_dict["lego's"] = 2
syllables_dict["subreddit's"] = 3
syllables_dict["reaper's"] = 2
syllables_dict['buzzkill'] = 2
syllables_dict['skims'] = 1
syllables_dict['tingles'] = 2
syllables_dict['pics'] = 1
syllables_dict['snowmen'] = 2
syllables_dict["plover's"] = 2
syllables_dict['faggotry'] = 3
syllables_dict['freakin'] = 2
syllables_dict['boogers'] = 2
syllables_dict['mewtwo'] = 2
syllables_dict["gaia's"] = 2
syllables_dict['subreddit'] = 3
syllables_dict['snowdrifts'] = 2
syllables_dict['tinnitus'] = 3
syllables_dict['swingset'] = 2
syllables_dict['rainclouds'] = 2
syllables_dict['backflow'] = 2
syllables_dict["jogger's"] = 2
syllables_dict['farts'] = 1
syllables_dict['birdwatch'] = 2
syllables_dict['sucky'] = 2
syllables_dict['epiphanies'] = 4
syllables_dict['unfillable'] = 4
syllables_dict['inverts'] = 2
syllables_dict['ziploc'] = 2
syllables_dict['kaiju'] = 2
syllables_dict['cis'] = 1
syllables_dict['deafens'] = 2
syllables_dict['slumbers'] = 2
syllables_dict['haha'] = 2
syllables_dict['cumshot'] = 2
syllables_dict["pretendin'"] = 3
syllables_dict['aang'] = 1
syllables_dict['phoenixes'] = 3
syllables_dict['scrolling'] = 2
syllables_dict['slacking'] = 2
syllables_dict['flagellation'] = 4
syllables_dict['sooths'] = 1
syllables_dict['simpletons'] = 3
syllables_dict["screen's"] = 1
syllables_dict['winrar'] = 2
syllables_dict['wingsuit'] = 2
syllables_dict['twitchy'] = 2
syllables_dict['astrovision'] = 4
syllables_dict['interweb'] = 3
syllables_dict['ziggy'] = 2
syllables_dict['pissing'] = 2
syllables_dict['upvoting'] = 3
syllables_dict['reddittors'] = 3
syllables_dict['savour'] = 2
syllables_dict["bed's"] = 1
syllables_dict['blooding'] = 2
syllables_dict['unties'] = 2
syllables_dict['scrubs'] = 1
syllables_dict['connectedness'] = 4
syllables_dict['dildo'] = 2
syllables_dict['starlings'] = 2
syllables_dict['turd'] = 1
syllables_dict['yaking'] = 2
syllables_dict['piggybacks'] = 3
syllables_dict['amps'] = 1
syllables_dict['tits'] = 1
syllables_dict["angle's"] = 2
syllables_dict['thrusted'] = 2
syllables_dict['dinkleberg'] = 3
syllables_dict['engulfs'] = 2
syllables_dict['hazed'] = 1
syllables_dict['poofs'] = 1
syllables_dict['dirtbag'] = 2
syllables_dict['windsurfing'] = 3
syllables_dict['maths'] = 1
syllables_dict['integrals'] = 3
syllables_dict['gerudo'] = 3
syllables_dict['distro'] = 2
syllables_dict['goldbond'] = 2
syllables_dict['simp'] = 1
syllables_dict['wiggles'] = 2
syllables_dict['doggo'] = 2
syllables_dict['tweets'] = 1
syllables_dict['ramen'] = 2
syllables_dict['birdsongs'] = 2
syllables_dict['bod'] = 1
syllables_dict['texting'] = 2
syllables_dict['narutp'] = 3
syllables_dict['cuddles'] = 2
syllables_dict['shitting'] = 2
syllables_dict['upended'] = 3
syllables_dict['teapots'] = 2
syllables_dict['adulting'] = 3
syllables_dict['chapstick'] = 2
syllables_dict['dork'] = 1
syllables_dict['cheetos'] = 2
syllables_dict['merch'] = 1
syllables_dict['slurping'] = 2
syllables_dict['pollinators'] = 4
syllables_dict['buttplug'] = 2
syllables_dict['binks'] = 1
syllables_dict['straightest'] = 2
syllables_dict['judgy'] = 2
syllables_dict['shat'] = 1
syllables_dict['blowjob'] = 2
syllables_dict['mins'] = 1
syllables_dict['om'] = 1
syllables_dict['ojos'] = 2
syllables_dict['tendrils'] = 2
syllables_dict['snitches'] = 2
syllables_dict['pickpocketing'] = 4
syllables_dict['shrek'] = 1
syllables_dict['cogs'] = 1
syllables_dict['meds'] = 1
syllables_dict['gurgles'] = 2
syllables_dict['bluetooth'] = 2
syllables_dict["i'mma"] = 2
syllables_dict['bedcovers'] = 3
syllables_dict['journaling'] = 3
syllables_dict['girthy'] = 2
syllables_dict['ritualize'] = 4
syllables_dict['extinguishes'] = 4
syllables_dict['broods'] = 1
syllables_dict['prowls'] = 1
syllables_dict['splayed'] = 1
syllables_dict['yoda'] = 2
syllables_dict['isopropyl'] = 4
syllables_dict['undressing'] = 3
syllables_dict['wasabi'] = 3
syllables_dict['seafloor'] = 2
syllables_dict['hypnotizing'] = 4
syllables_dict['sticked'] = 1
syllables_dict['moonless'] = 2
syllables_dict['uncorking'] = 3
syllables_dict['yumminess'] = 3
syllables_dict['zit'] = 1
syllables_dict['creaks'] = 1
syllables_dict['singularity'] = 5
syllables_dict['vanquishing'] = 3
syllables_dict['dunking'] = 2
syllables_dict['clenching'] = 2
syllables_dict['hairtie'] = 2
syllables_dict['clacks'] = 1
syllables_dict['bitcoin'] = 2
syllables_dict['layed'] = 1
syllables_dict['reconsiders'] = 4
syllables_dict['canopies'] = 3
syllables_dict['meetup'] = 2
syllables_dict['shadowless'] = 3
syllables_dict['sativa'] = 3
syllables_dict['paperclip'] = 3
syllables_dict['ogres'] = 2
syllables_dict['overwatch'] = 3
syllables_dict['smudges'] = 2
syllables_dict["'nother"] = 2
syllables_dict['clovers'] = 2
syllables_dict['passionfruit'] = 3
syllables_dict['grazes'] = 2
syllables_dict['pikachu'] = 3
syllables_dict['stormwater'] = 3
syllables_dict['maskless'] = 2
syllables_dict['doggin'] = 2
syllables_dict['scuttles'] = 2
syllables_dict['resurfaces'] = 4
syllables_dict['faggoted'] = 3
syllables_dict['crosshairs'] = 2
syllables_dict['retching'] = 2
syllables_dict['dumbass'] = 2
syllables_dict['undead'] = 2
syllables_dict['tumblr'] = 2
syllables_dict['trashcan'] = 2
syllables_dict['snapchat'] = 2

# scraping some website for its (questionable) info:
import requests

from bs4 import BeautifulSoup
from syllables import syllable

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

# creating url and requests instance
def scrape(url):
    try:
        html = session.get(url)
    except requests.exceptions.ConnectionError:
        raise Exception("Connection Error!")

    # getting raw data
    soup = BeautifulSoup(html.text, 'html.parser')

    # print(soup.prettify())
    page_strings = [x.string for x in soup.find_all('a')]
    words = []
    start = False
    for string in page_strings:
        if string == 'Z' and start is False:
            start = True
            continue
        if start is False:
            continue
        if string is None:
            break
        if len(string.split()) == 1:
            words.append(string)
    # print(words[:10])
    return words

syllable_list = []
for i in range(15):
    syllable_list.append(scrape(f'https://syllablecounter.io/words/{i+1}-syllable-words'))


d = [(k, i) for (i, k) in enumerate(syllable_list)]
e = []
for word_list, count in d:
    for word in word_list:
        e.append((word, count+1))

mydict = dict(e)

syllables_dict = {**syllables_dict, **mydict}

# saving out to a file
with open('syllable_dictionary.json', 'w') as f:
    json.dump(dict(sorted(syllables_dict.items())), f)
