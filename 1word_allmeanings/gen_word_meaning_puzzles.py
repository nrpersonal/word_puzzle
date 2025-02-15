import random
import os, sys

# Sample dictionary with words and multiple comma-separated meanings
word_dict = {
'Affluent':'rich prosperous wealthy thriving',
'Destitute':'poor penniless needy',
'Naïve':'simple innocent inexperienced',
'Novice':'beginner trainee apprentice',
'Leer':'stare ogle',
'Jeer':'mock taunt ridicule insult scorn',
'Tarmac':'tar pitch runway',
'Alter':'change modify amend',
'Flume':'torrent waterfall',
'Sew':'stich embroidery seam hem',
'Rover':'traveller vagrant vagabond nomad',
'wanderer':'tramp',
'Perm':'curl wave fizz',
'Pottery':'clay ceramics earthenware',
'China':'dishes plates porcelain',
'Downpour':'rainstorm deluge heavy shower',
'Torrent':'gush flood surge deluge',
'Reap':'grow acquire procure cultivate',
'Rapid':'fast speed hasty hurried swift',
'Rattle':'bang clatter',
'Cuddle':'embrace clasp hold fondle snuggle',
'Arena':'stadium pitch ground',
'Apex':'summit peak top zenith pinnacle',
'Idle':'motionless stationary indolent sluggish',
'Idol':'star celebrity hero',
'Tendon':'muscle ligament Cartilage',
'Fault':'error responsibility liability blunder',
'Tremor':'shake turbulence tremble quake shock',
'Steeple':'tower highest point of the church',
'Vicar':'priest monk preacher minister parson',
'Generous':'lavish plenty substantial liberal spendthrift',
'Selfish':'self-centred egoistic greedy',
'Moor':'grasslands hill upland moorland heath hillock lea',
'Witty':'funny clever droll amusing',
'Umpire':'referee mediator',
'Jockey':'rider equestrian',
'Bloom':'blossom flower flourish thrive grow develop',
'Restore':'repair fix rebuild',
'Fare':'cost fee price tariff toll',
'Habit':'custom routine practice tradition pattern',
'Drudge':'slave toil worker labour slog',
'Dodge':'avoid escape duck evade elude',
'Perform':'act play',
'Dome':'vault cupola roof ceiling',
'Trawl':'scan rummage seek probe investigate hunt search scrutinising',
'Shaft':'tube channel trough',
'Thrust':'shove push prod plunge stab insertion',
'Fraction':'part fragment piece portion segment element',
'Accelerate':'hurry hasten quicken rush',
'Tepid':'lukewarm',
'Elaborate':'extravagant ornate decorative elegant',
'Hostile':'unfriendly antagonistic aggressive',
'Thaw':'defrost melt liquify soften',
'Trim':'prune crop cut clip',
'Stain':'tinge dye colour tint pigment',
'Smear':'mark blotch stain insult slur',
'Deter':'stop discourage prevent frighten',
'Inferno':'fire blaze furnace firestorm',
'Hank':'coil reel length bundle ball',
'Strand':'thread element component part filament fibre',
'Recent':'modern fresh latest current novel',
'Latter':'end final concluding later',
'Former':'previous past ex last prior',
'Pursue':'chase hunt trail track tail shadow follow',
'Fragile':'delicate flimsy brittle breakable frail puny',
'Aroma':'smell fragrance perfume scent whiff odour',
'Blurt':'cry utter announce revel divulge',
'Chant':'sing tune hymn mantra recite repeat',
'Limb':'branch bough appendage',
'Grit':'gravel shingle sand dirt pebbles stones',
'Wind':'gale gust breeze',
'Tempest':'storm hurricane cyclone gale',
'Meadows':'fields pastures paddocks ( where horses are trained) leas',
'Bleach':'whiten lighten decolourize blanch',
'Rural':'countryside rustic pastoral',
'Urban':'city town borough',
'Fend':'defend',
'Feign':'fake pretend assume sham',
'Dawdle':'linger delay loiter plod',
'Punctual':'prompt on time',
'Defer':'accept submit comply bow down',
'Amiable':'friendly sociable affable likable',
'Bland':'tasteless mild plain flavourless',
'Weary':'tired fatigue drained drowsy Knackered worn out',
'Dreary':'dull boring monotonous tedious lifeless routine Mundane',
'Deck':'surface floor',
'Scum':'dirt crust layer froth',
'Litter':'disorder confusion mess clutter rubbish',
'Shield':'protection armour defence buffer',
'Tamper':'interfere meddle fiddle interrupt',
'Sear':'burn scorch singe char',
'Amendment':'alter modify change correct',
'Parched':'thirsty gasping dehydrated',
'Preserve':'conserve jam sustain',
'Lent':'borrowed rented hired loaned',
'Mound':'hill mount dune hillock',
'Bough':'branch limb spur',
'Heed':'notice attention note regard',
'Bashful':'shy reserved timid meek mild',
'Paramount':'important dominant utmost significant',
'Capsized':'overturned tipped sank',
'Shrub':'bush plant climber',
'Craft':'skill expertise ability',
'Gullible':'trusting naïve innocent',
'Docile':'mild passive quite meek obedient',
'Lounge':'living room family room sitting room',
'Foil':'stop frustrate hinder outwit',
'Bellow':'shout roar yell bawl holler Row',
'Hurl':'throw fling toss chuck launch',
'Haul':'tow drag pull lug heave',
'Fringe':'border outlying frontier',
'Descent':'decline decrease',
'Peach':'fruit colour beauty wow',
'Launch':'presentation introduction take-off departure',
'Uprising':'rebel rising revolt unrest disturbance',
'Affable':'jovial sociable genial friendly Amicable',
'Charitable':'generous giving liberal',
'Mandatory':'obligatory Compulsory required',
'obligatory':'necessary essential',
'Clarity':'clearness lucid transparency',
'Dormant':'inactive sleeping resting',
'Pristine':'clean immaculate unspoiled perfect Spotless',
'Converse':'reverse inverse contrary opposing opposite',
'Poach':'rob steal thieve',
'Crude':'basic unpolished amateur simple rough unfinished unskilful Rookie',
'Intermediate':'middle midway mean in between',
'Tactful':'sensitive thoughtful considerate discreet diplomatic',
'Futile':'useless pointless fruitless vain wasted',
'Adore':'love worship esteem respect admire',
'Adorn':'decorate garnish ornament',
'Detest':'hate loathe despise Abor',
'Vague':'unclear faint ambiguous imprecise indefinite',
'Dolly':'model puppet toy figure',
'Spectator':'viewer watcher observer witness',
'Ladle':'spoon scoop dipper server',
'Suit':'outfit costume uniform ensemble',
'Rind':'peel skin husk crust coat',
'Urn':'pot container vessel pitcher jug',
'Warren':'den hole earth habitat burrow lair',
'Seldom':'rarely infrequently occasionally hardly',
'Concur':'agree correspond harmonize coincide*',
'Conceal':'misplace hidden',
'Truce':'make peace lull',
'Dainty':'delicate elegant graceful exquisite refined petite',
'Estimate':'guess crock',
'Bash':'party celebration gala',
'Perceive':'observe notice remark distinguish recognise',
'Arrogant':'big headed superior conceited',
'Animated':'active lively energetic vigorous vibrant dynamic spirited',
'Tentative':'hesitant cautious uncertain unsure',
'Reject':'discard castoff',
'Swagger':'boastfulness boasting bragging arrogance',
'Moral':'ethical good right honest honourable jus virtuous',
'Corrupt':'dishonest crooked unethical immoral',
'Daunt':'scare frighten overwhelm discourage deter',
'Safari':'expedition voyage trip excursions outins journey',
'Menace':'risk danger threat peril Hazard dangerous peril',
'Wreckage':'debris ruin wreck rubble remains',
'Freight':'cargo load goods',
'Crease':'wrinkle crinkle rumple crumple',
'Saunter':'sprint stroll walk ramble amble meander',
'Rowdy':'noisy unruly loud disorderly boisterous raucous disruptive',
'Audible':'easy to hear distinct clear loud',
'Conspire':'plot scheme plan',
'Frivolousnot':'seriousplayful frolicsome perky silly flippant',
'Lenient':'kind forgiving mild moderate tolerant easy going',
'Rectify':'amend correct alter',
'Droop':'sag wilt bow flop sink slouch',
'Hoard':'store pile mass reserve stockpile stash',
'Vigilant':'watchful attentive alert wary cautious observant heedful aware',
'Retain':'recall recollect remember hold preserve',
'Opponent':'enemy foe rival challenger adversary ally',
'Valour':'courage bravery spirit nerve fearless boldness gallantry heroic pluck',
'Decline':'decay lessen drop deteriorate decrease',
'Elevator':'going up',
'Earnest':'serious grave sober genuine solemn',
'Terminate':'end conclude sack axe fire dismiss',
'Gather':'assemble congregate collect',
'Scarcity':'shortage lack dearth scanty meagre',
'Agile':'swift nimble alert responsive lively',
'Supple':'soft flexible mobile elastic',
'Retreat':'recoil withdraw evacuate flee',
'Protrude':'jut out overhang bulge swell',
'Wail':'howl moan scream cry yelp whine',
'Lisp':'Speech difficulty slutter',
'Treasured':'cherished beloved precious',
'Dear':'expensive beloved',
'Thrifty':'miserly careful frugal economical cheap',
'Glory':'brilliance beauty wonder splendour',
'Malady':'ailment illness sickness disorder condition',
'Ancestor':'forefather',
'Pantry':'food storage storeroom',
'Serious':'grave solemn sombre grim sober',
'Satisfied':'content',
'Negligent':'carless thoughtless',
'Souvenir':'memento keepsake',
'Donation':'offering',
'Tranquillity':'harmony serene calm sanctuary refugee',
'Hoax':'trick',
'Persuade':'coax entice',
'Vigorous':'energetic dynamic active robust',
'Altitude':'height lofty elevation',
'Strike':'hit pound punch',
'Replicate':'copy mimic imitate',
'Trivial':'unimportant small penalty fine petty',
'Opaque':'unclear cloudy muddy misty smoky dense',
'Scurry':'scramble dash hurry fast',
'Detour':'diversion deviation',
'Jealous':'envious bitter green-eyed resentful',
'Diminish':'lessen contract',
'Infectious':'contagious catching transmittable',
'Warrior':'solider trooper fighter',
'Speckled':'dotted freckled',
'Inlet':'creek bay cove',
'Heave':'throw hurl toss',
'Perimeter':'edge rim border boundary circumference',
'Athletic':'sporty healthy agile nimble energetic',
'Spry':'lively agile nimble active brisk',
'Indolent':'lazy lethargic idle sluggish',
'Insolent':'rude impudent disrespectful',
'Legible':'readable clear understandable',
'Elevate':'raise lift uplift hoist upraise',
'Diligent':'hardworking industrious assiduous',
'Ale':'beer drink alcohol',
'Log':'diary journal calendar logbook record',
'Grumpy':'irritable bad-tempered cranky sullen',
'Miffed':'annoyed',
'Bid':'offer',
'Moat':'a deep wide ditch',
'Lance':'a long pointed rod used as weapon',
'Shallow':'superficial not-deep',
'Еmu':'a Type of Beid like Oftich',
'Ire':'anger rage fury wrath temper',
'Blotted-out':'Blocked-out Disappear e.g.The-grey-clouds-blotted-out-the-sun',
'Merry':'gleeful Joyful cheful excited',
'Scruting':'sepection',
'clad':'Dressed(people) Covered(things)',
'Perch':'For-bird-means-sit-rest-or-alight for-person-means-sit-on-something for-Building-means-be-situated-or-located',
'Dilapidated':'Broken-down shabby Ramshackle battered Rickety worn-out In-need-of',
'Burgenoing':'growing increasing Expanding',
'Unease':'anxious Stressed unconfortable',
'Solemnly':'seriously',
'gay':'Cheesful',
'Abide':'Obey follow accept',
'Remorse':'Regret guilt',
'Wretch':'villain criminal unhappy person',
'Doom':'Death Destruction',
'Relentles':'merciless pitiless',
'Emboldened':'enconrage-by-something',
'Din':'loud noise clang clamour clatter del',
'Dame':'an-elderly-or-Mature-woman',
'Rack':'Storm',
'To-exult':'to-rejoice  be-delighted',
'keel':'the-underside-of-a-ship',
'Squand':'to waste misuse to-spend-foolishly',
'Grim':'dingy dull Very-serious',
'Flora':'and Fauna Plants-and-animals',
'Dwindling':'gradually-decrease-in-Size-or-amount-or-strength',
'Inadvertently':'unintentionally accidently By-mistake',
'Habitat':'home nalural Environment Abode',
'Deduce':'infer guess surmise calculate draw conclusion',
'Satchel':'A-Bag-with-a-long-strap.',
'Rifled':'Search-quickly-through-Something.',
'Contemplated':' thinking deep-thought remembering-past',
'Vicked':'cut scratch',
'Intimidating':'',
'frightening':'targar area',
'Sprawling':' Spreading-out-over-a-larger-area',
'Inquisitive':'curious interested intrusive Concerned',
'Bustling':'Crowded',
'winding':' cuvys Twisting',
'Haggle':'  Bargain',
'Array':'range types Variety',
'Enchant':'attractive',
'Enthral':'Interested',
'Culinary':'cookingskills',
'Overlooking':'have-a-view-from-above-or-balcony-overlooking-the-rivere',
'Ceremonial':'Ritual events religions',
'Encounter':'meet come-across run-into stumble-upon bump-into meet-by-chance',
'Sycamore':'Type-of-tree',
'Trees':'Elm Ash Oak Fir sycamore leak',
'Nestles':'location situated placed',
'Obscure':'Unclear',
'petty':'trivial small negligible insignificant',
'Stems':'origin start root',
'Quirks':'Peculiarity',
'Glut':'too-many too-much excess abundant surplus',
'Boasts':'gloats show-off brag',
'Amples':'lots-of many plenty',
'Bespoke':'Custom-made made-to-order bespoke-place-or-thing made-for-you',
'Accolade':'awarded recognition honour',
'imminent':'Happening-soon about-to-happen close near forthcoming on-the-way',
'Renowned':'Famous illustrious prominent great',
'Vanquish':'to-Conquer to-overcome',
'Rean':'to-widen to-criticize',
'State':'government polities',
'Futurstic':'ahead-of-time in-future',
'Marred':'Spoiled ruin disfigure',
'Irate':'angry furious fuming enraged',
'Unsuly':'Rowdy noisy wild disobedient',
'Chaotic':'turmoil disorderly confused chaos disarray messy',
'Subsidise':'Reduce less decrease',
'vociferous':'vocal frank candid open direct eager vehement',
'Inevitably':'unavoidable assured certain fated sure necessary',
'Intellectual':'intelligence mental cerebral cognitive rational conceptual',
'Revenue':'income takings receipts profit earnings returns',
'Income-tax':'tax-levied-on-income',
'Gusto':'with-enjoyment',
'Shabby':'scruffy Dingy wornout',
'Agape':'wide-open-mouth-in-surprise-or-wonder',
'Seek(sought)':'Look-for pursue go-after attemptask-for',
'Squander':'to-waste',
'Victor':'Victorious triumphant Succeseful'
}

# Function to split dictionary into chunks of 20 words
def split_dict_into_chunks(dictionary, chunk_size=20):
    items = list(dictionary.items())
    return [dict(items[i:i+chunk_size]) for i in range(0, len(items), chunk_size)]

# Function to generate and save the matching puzzle
def generate_puzzle_files(word_chunks):
    os.makedirs("puzzles", exist_ok=True)  # Create folder for puzzles
    os.makedirs("answers", exist_ok=True)  # Create separate folder for answers
    for idx, chunk in enumerate(word_chunks, 1):
        words = list(chunk.keys())
        meanings = [meaning.strip() for word in chunk.values() for meaning in word.split(",")]
        
        random.shuffle(meanings)  # Shuffle meanings to make the puzzle hard
        meaning_dict = {chr(97 + i): meaning for i, meaning in enumerate(meanings)}  # Assign 'a', 'b', 'c'...

        # Generate correct answer key
        correct_answers = {word: [key for key, meaning in meaning_dict.items() if meaning in chunk[word]] for word in words}
        # Save puzzle in puzzles directory
        puzzle_filename = f"puzzles/puzzle_{idx}.txt"
        with open(puzzle_filename, "w", encoding="utf-8") as puzzle_file:
            puzzle_file.write("Match the words to their correct meanings:\n\n")   
           
            # Print words and their corresponding shuffled meanings side by side
            for i, (word, key) in enumerate(zip(words, meaning_dict.keys()), 1):
                puzzle_file.write(f"{i}. {word:<15} {key}) {meaning_dict[key]}\n")
        print(f"Puzzle saved: {puzzle_filename}")

        # Save answers in answers directory
        answer_filename = f"answers/answer_{idx}.txt"
        with open(answer_filename, "w", encoding="utf-8") as answer_file:
            answer_file.write("Answer Key:\n\n")
            for word, keys in correct_answers.items():
                answer_file.write(f"{word} -> {', '.join(keys)}\n")
        print(f"Answer key saved: {answer_filename}")


# Split dictionary and generate puzzles
try:
    size=len(word_dict)
    print(f'Starting Execution: wordlist is of size {size}')
    if(size > 0):
        word_chunks = split_dict_into_chunks(word_dict, 20)
        generate_puzzle_files(word_chunks)
except Exception as e:
          exc_type, exc_obj, exc_tb = sys.exc_info()
          fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          print(f'We have a failure processing output_txt -> Reason: {e}, exc_type: {exc_type}, fname: {fname}, exc_tb.tb_lineno: {exc_tb.tb_lineno}') 
 


