import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def render(game,current):
        '''Display the current room, moves, and points'''
        r = game['rooms']
        c = r[current]
        return True
        print('\n\nYou are in the {name}'.format(name=c['name']))
        print(c['desc'])

def update(selection,game,current):
    '''Update our location, if possible, etc. '''
    for e in game['rooms'][current]['exits']:
        if e['verb'] == response:
            current = e['target']
    return True

def check_input():
    '''Asks the user for input'''
    response = input('\nWhat would you like to do? ').strip().upper()
    return response

def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'

quit = False

while not quit:
    
    render(game,current)

    
    selection = getInput()

    
    current = update(selection,game,current)
    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()