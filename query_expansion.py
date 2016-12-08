import string
import settings


#perbanyak lagi
locations = list(settings.cities_dict) + list(settings.provinces_dict)

#perbanyak lagi
categories = ["Monuments & Statues", "Food & Drink", "Karaoke Bars", "Sacred & Religious Sites", "Other Outdoor Activities", "Other Nature & Parks", "Art Museums", "Caverns & Caves", "Other Fun & Games", "Bodies of Water", "Arenas & Stadiums", "Zoos & Aquariums", "Specialty Museums", "Valleys", "Nightlife", "Ancient Ruins", "Eco Tours", "Playgrounds", "Department Stores", "Flea & Street Markets", "Piers & Boardwalks", "Fun & Games", "More", "History Museums", "Shopping", "Water & Amusement Parks", "Ferries", "Water Parks", "Neighborhoods", "Shopping Malls", "Biking Trails", "Museums", "City Tours", "Concerts & Shows", "Waterfalls", "Traveler Resources", "Islands", "Golf Courses", "Other Zoos & Aquariums", "Antique Stores", "Reefs", "Volcanos", "restaurant", "Sights & Landmarks", "Nature & Parks", "Farms", "Tours", "Factory Outlets", "Bridges", "Boat Rentals", "Boat Tours & Water Sports", "Observation Decks & Towers", "Thermal Spas", "Private Tours", "Mountains", "Transportation", "Points of Interest & Landmarks", "Theme Parks", "Gift & Specialty Shops", "Churches & Cathedrals", "Parasailing & Paragliding", "Spas & Wellness", "Sightseeing Tours", "Lookouts", "Conference & Convention Centers", "Cultural Tours", "Castles", "Jogging Paths & Tracks", "Outdoor Activities", "National Parks", "Forests", "Libraries", "halal", "Motorcycle Trails", "Nature & Wildlife Tours", "Cemeteries", "State Parks", "Farmers Markets", "Nature & Wildlife Areas", "Mass Transportation Systems", "Beaches", "Scuba & Snorkeling", "Historic Sites", "Sports Complexes", "Gardens", "Hiking Trails", "Bars & Clubs", "Other Food & Drink", "Architectural Buildings", "Hot Springs & Geysers", "Ballets"]
syns = ['axles', 'nurseries', 'colleges', 'exhibitions', 'technologies', 'tombs', 'wetlands', 'four', 'facilities', 'farms', 'woods', 'tours', 'cooperative', 'skin', 'fixtures', 'adjustment', 'religious', 'centers', 'votes', 'graves', 'fellowship', 'segments', 'monasteries', 'periodicals', 'gigs', 'riders', 'carnivals', 'bays', 'contours', 'dirty', 'include', 'presentation', 'meadows', 'resources', 'hill', 'washroom', 'activities', 'labels', 'premium', 'recitals', 'homes', 'perishable', 'bulletin', 'railways', 'retailers', 'vegan', 'cemeteries', 'street', 'cellular', 'cook', 'clearings', 'precinct', 'alpine', 'recreation', 'magic', 'prize', 'solutions', 'yachting', 'crops', 'positions', 'companies', 'kiosks', 'standards', 'race', 'Halal', 'relics', 'car', 'radio', 'hostels', 'landlords', 'ornamental', 'spiritual', 'neighborhood', 'pledge', 'core', 'tea', 'traveler', 'cyber', 'layouts', 'titles', 'carriages', 'perspective', 'pans', 'licenses', 'cloisters', 'birdwatching', 'scientific', 'mausoleums', 'swamps', 'domestic', 'public', 'indian', 'poles', 'new', 'net', 'European', 'plush', 'lowlands', 'transportation', 'commercial', 'ramps', 'lakes', 'water', 'hubs', 'tracks', 'pickets', 'bamboos', 'aid', 'LSTs', 'canals', 'steamships', 'hoops', 'bakeries', 'biodiversity', 'items', 'vegetarian', 'casino', 'sustainability', 'fortresses', 'museums', 'miniature', 'airport', 'base', 'products', 'social', 'priceless', 'weird', 'anthropological', 'rafting', 'climber', 'coastline', 'lighthouses', 'hilltops', 'fantastic', 'tasks', 'addresses', 'humour', 'hedgerows', 'transit', 'precincts', 'private', 'bullock', 'screens', 'marvelous', 'busses', 'topographical', 'refreshment', 'cities', 'residences', 'ballets', 'festivals', 'woodland', 'tools', 'cloud', 'hotels', 'literary', 'from', 'sunbathing', 'lockers', 'two', 'coffeehouses', 'rustic', 'leaks', 'bike', 'music', 'archives', 'characteristics', 'scope', 'chateaux', 'markets', 'more', 'fragmentary', 'walkways', 'holy', 'towers', 'carvings', 'waterways', 'wildlife', 'forests', 'plantations', 'campsites', 'factories', 'karaoke', 'town', 'organizations', 'balls', 'mythical', 'allotments', 'science', 'inertial', 'districts', 'movies', 'locker', 'regions', 'publications', 'island', 'ferry', 'pickle', 'choirs', 'piers', 'history', 'crazy', 'bogs', 'hamburger', 'speciality', 'baronies', 'galleries', 'sentries', 'sample', 'skydiving', 'minimum', 'fanciful', 'quartets', 'woodlands', 'sense', 'databases', 'intramural', 'information', 'educational', 'backpacking', 'worldview', 'technology', 'Concerning', 'boxing', 'ledges', 'hillsides', 'traders', 'liveries', 'hot', 'townlands', 'forest', 'sacred', 'beach', 'taverns', 'stock', 'rinks', 'poker', 'regional', 'ballroom', 'hog', 'farm', 'mangroves', 'communal', 'lab', 'entrepreneurship', 'applications', 'paintball', 'district', 'adventure', 'records', 'vases', 'seashells', 'authentic', 'racks', 'gorges', 'lifesaving', 'branches', 'athletics', 'commodity', 'light', 'conglomerates', 'provinces', 'lines', 'volleyball', 'tulip', 'bakery', 'civics', 'truck', 'villas', 'banks', 'rentals', 'athletes', 'bungee', 'wine', 'displays', 'theme', 'neighbourhoods', 'concertos', 'hierarchy', 'lithographic', 'astronomical', 'thermal', 'through', 'costume', 'condominiums', 'bulldozers', 'cold', 'rocks', 'journals', 'industries', 'bridges', 'entrances', 'gymnastic', 'masses', 'recreational', 'racecar', 'nostalgia', 'isolation', 'better', 'trams', 'permanent', 'dwellings', 'savory', 'hobby', 'soccer', 'parades', 'artisanal', 'pedagogical', 'coffee', 'geysers', 'food', 'practice', 'nation', 'shuttle', 'walls', 'safari', 'hands', 'flea', 'clouds', 'oratorios', 'airports', 'greenhouses', 'agro', 'fundraisers', 'grasslands', 'kayaking', 'sailor', 'swimsuit', 'fairs', 'courses', 'picnics', 'lingerie', 'lofts', 'paddling', 'pools', 'entirely', 'cliffs', 'manors', 'concerts', 'volcanos', 'bicycle', 'schemes', 'From', 'busts', 'fish', 'prawn', 'polychrome', 'society', 'overpasses', 'dubstep', 'corporations', 'laboratory', 'teams', 'amusement', 'projections', 'initiatives', 'marketplaces', 'alcohol', 'entertainment', 'catacombs', 'boutique', 'factory', 'hydraulic', 'adhesion', 'participants', 'playground', 'sightseeing', 'induction', 'brewery', 'shows', 'foundation', 'eco', 'closings', 'merchants', 'waterfalls', 'waterbirds', 'depots', 'labs', 'houses', 'snooker', 'basketball', 'campgrounds', 'birding', 'mudflats', 'uplands', 'scary', 'dormitories', 'milestones', 'benefits', 'equine', 'shelves', 'habitats', 'miners', 'modules', 'ministries', 'plane', 'palaces', 'reels', 'rainforest', 'synagogues', 'picnicking', 'initial', 'features', 'ethical', 'attractions', 'softball', 'trackways', 'bazaars', 'wash', 'philosophical', 'establishments', 'agri', 'abutments', 'inns', 'cups', 'temples', 'city', 'story', 'ancient', 'publication', 'service', 'festival', 'grilles', 'influence', 'engagement', 'traveller', 'rails', 'hollows', 'boating', 'philanthropy', 'conservation', 'parasailing', 'trails', 'structures', 'store', 'interests', 'lottery', 'releases', 'watersports', 'academy', 'gym', 'hotel', 'motorcycle', 'tombstones', 'environmental', 'optical', 'rickshaw', 'spas', 'albums', 'flowers', 'ecotourism', 'gambler', 'viaducts', 'pillboxes', 'cracks', 'sculptures', 'hammocks', 'boring', 'volcanoes', 'dikes', 'youth', 'headlands', 'fabulous', 'historical', 'trekking', 'fishermen', 'chalets', 'scuba', 'spurs', 'interactive', 'and', 'bridge', 'topics', 'modern', 'locations', 'buildings', 'raw', 'childcare', 'halal', 'stalls', 'breakfast', 'organs', 'seminar', 'paths', 'constructions', 'handicraft', 'cottages', 'shorts', 'subdivisions', 'parks', 'dining', 'rehearsals', 'subjects', 'luxury', 'doors', 'transnational', 'tunnels', 'jungle', 'villages', 'multiple', 'equestrian', 'theatre', 'centre', 'singles', 'cathedrals', 'sets', 'troughs', 'complexes', 'intergalactic', 'lists', 'convents', 'engagements', 'sinkholes', 'artefacts', 'observation', 'neighborhoods', 'lessons', 'boardwalks', 'performances', 'coves', 'snowmobiling', 'bookstore', 'artistic', 'mechanical', 'brew', 'professional', 'salt', 'institutions', 'goals', 'sector', 'reefs', 'hiking', 'golf', 'cruises', 'formal', 'indoor', 'sites', 'bookings', 'colors', 'session', 'businesses', 'shoe', 'midwife', 'cabins', 'boutiques', 'networks', 'ground', 'toast', 'knowledge', 'peasants', 'basilicas', 'ruin', 'striptease', 'sugar', 'only', 'rice', 'local', 'cockpits', 'shepherd', 'monuments', 'canyons', 'sights', 'secular', 'railings', 'dry', 'maritime', 'fortifications', 'minarets', 'churches', 'breakbeat', 'leases', 'botanical', 'requirement', 'areas', 'tobacco', 'wellness', 'workman', 'performers', 'nutritious', 'alteration', 'marinas', 'perfume', 'sacrifices', 'monumental', 'architecture', 'activity', 'murals', 'ruins', 'vision', 'restaurants', 'lettering', 'bars', 'official', 'art', 'concert', 'psychological', 'national', 'fable', 'startup', 'emergent', 'culture', 'electrostatic', 'sparkling', 'changes', 'parking', 'sport', 'SCUBA', 'points', 'seminaries', 'vents', 'cosplay', 'camping', 'farmers', 'pictures', 'swimwear', 'hatcheries', 'libraries', 'premises', 'state', 'future', 'various', 'furnishings', 'conceptual', 'sanctuaries', 'caves', 'numerous', 'decks', 'corridors', 'carbonated', 'infrastructure', 'enclosures', 'nature', 'importance', 'franchises', 'volumetric', 'souvenir', 'offices', 'affiliates', 'premise', 'angling', 'regular', 'rodeos', 'mariner', 'congregations', 'sanitation', 'restaurant', 'country', 'cafes', 'reliefs', 'presentations', 'trips', 'kosher', 'players', 'kitchens', 'figures', 'auctions', 'midwifery', 'searchlights', 'statues', 'fields', 'ranchers', 'basins', 'snowshoeing', 'caverns', 'venues', 'ballparks', 'church', 'springs', 'regenerative', 'boat', 'bingo', 'arts', 'packages', 'cycling', 'motorbike', 'icebergs', 'union', 'dams', 'political', 'three', 'chimneys', 'suburbs', 'secret', 'viticulture', 'maintenance', 'basic', 'linguistic', 'fry', 'exhibition', 'cutouts', 'placenames', 'life', 'tournament', 'shopping', 'counselling', 'sectors', 'blessing', 'enterprises', 'convention', 'wrestling', 'orchestras', 'systems', 'standup', 'cantatas', 'towns', 'sticky', 'spirit', 'locales', 'divisions', 'arias', 'atmospheric', 'adaptations', 'stadia', 'frozen', 'tribal', 'entrepreneurial', 'programme', 'policies', 'fun', 'curricula', 'shops', 'biking', 'dykes', 'vaults', 'lodges', 'aquaria', 'playgrounds', 'canoeing', 'canoe', 'almost', 'soil', 'spectacle', 'workplaces', 'surface', 'Oah', 'refinery', 'soils', 'arrangements', 'malls', 'baths', 'arenas', 'restroom', 'musicals', 'movements', 'blockhouses', 'different', 'grandiose', 'dairies', 'marshlands', 'stadiums', 'vintage', 'landmarks', 'parishes', 'jogging', 'scooter', 'matches', 'periodic', 'sidecar', 'regattas', 'units', 'games', 'colonies', 'events', 'sled', 'development', 'oil', 'temporary', 'fraternity', 'assignment', 'drink', 'parkways', 'opulent', 'cafeterias', 'pubs', 'levels', 'architectures', 'rockabilly', 'cityscape', 'tuna', 'magician', 'residents', 'lacrosse', 'noodle', 'theater', 'scenario', 'programs', 'navigation', 'cultural', 'motorcycling', 'materials', 'components', 'centres', 'theatres', 'traffic', 'laboratories', 'corporate', 'investments', 'bodies', 'scholarship', 'seasonal', 'gates', 'outdoor', 'stores', 'livestock', 'just', 'less', 'barbecues', 'embankments', 'biodegradable', 'restrooms', 'communities', 'madrigals', 'cays', 'provincial', 'seats', 'tone', 'startups', 'stairways', 'assemblages', 'hills', 'localities', 'watchtowers', 'residential', 'shrines', 'international', 'bookshops', 'location', 'wet', 'openings', 'transformation', 'eateries', 'government', 'docks', 'Chinatown', 'architectural', 'warehouse', 'boxes', 'historic', 'five', 'community', 'barge', 'performance', 'castings', 'world', 'execution', 'projects', 'meat', 'county', 'clam', 'mansions', 'ramparts', 'schools', 'concerti', 'gyms', 'miracle', 'intercollegiate', 'physiotherapy', 'zoos', 'wineries', 'vegetation', 'Chinatowns', 'paragliding', 'soft', 'directories', 'imprints', 'names', 'classes', 'valleys', 'shuttles', 'village', 'magnificent', 'competition', 'platforms', 'clubs', 'productions', 'ornaments', 'images', 'contests', 'bindings', 'transport', 'chorus', 'humor', 'for', 'dunes', 'colonial', 'legal', 'passageways', 'competitions', 'tramways', 'dealership', 'sledding', 'pattern', 'panes', 'conference', 'recyclable', 'medieval', 'prairies', 'terraces', 'bathhouses', 'outlets', 'stew', 'lounges', 'crap', 'pumps', 'properties', 'beaches', 'gears', 'picnic', 'actual', 'boards', 'imprompt', 'of', 'newspapers', 'lookouts', 'nightclub', 'dinner', 'involving', 'economic', 'corals', 'islands', 'concession', 'homesteads', 'windsurfing', 'road', 'pollution', 'antique', 'primitive', 'memorials', 'wilderness', 'interruption', 'whites', 'landowners', 'vacation', 'fishes', 'stalactites', 'jet', 'roads', 'episodes', 'lesson', 'sports', 'revues', 'steamboats', 'canteens', 'infrastructures', 'grids', 'shires', 'area', 'grapevine', 'museum', 'tennis', 'fundraiser', 'gift', 'fast', 'custom', 'parachute', 'workshop', 'abbeys', 'stars', 'amenities', 'girders', 'leagues', 'mountains', 'Regarding', 'medium', 'interest', 'SeaWorld', 'capability', 'volunteerism', 'workshops', 'specialty', 'fountains', 'slums', 'cores', 'fisheries', 'archaic', 'sardine', 'staircases', 'library', 'crane', 'calico', 'shutters', 'patriot', 'dowry', 'comics', 'breweries', 'artisans', 'authority', 'clips', 'carriage', 'sponsorships', 'nightlife', 'winery', 'casts', 'flats', 'panels', 'landscapes', 'circuses', 'Townsville', 'castles', 'rapids', 'wellbeing', 'circus', 'urns', 'covers', 'evidence', 'reservoirs', 'mountaineering', 'field', 'ship', 'cafe', 'yearbook', 'dealer', 'shit', 'programmes', 'bicycling', 'storage', 'aquariums', 'application', 'other', 'electrical', 'snorkeling', 'tugboats', 'department', 'depot', 'smell', 'potential', 'revision', 'suites', 'operettas', 'congress', 'theatrical', 'ravines', 'narrative', 'utilities', 'diet', 'apparel', 'ecological', 'midget', 'pathways', 'marshes', 'ferries', 'brands', 'depicting', 'stocks', 'strips', 'seamounts', 'land', 'assets', 'amusements', 'forts', 'foundry', 'departments', 'stacks', 'beds', 'hikes', 'beverage', 'mass', 'rallies', 'orphanages', 'rural', 'banners', 'songs', 'mosaics', 'gardens', 'once']


syns_to_cat = {'axles': 51, 'nurseries': 61, 'colleges': 71, 'exhibitions': 74, 'technologies': 79, 'tombs': 66, 'wetlands': 78, 'four': 87, 'facilities': 88, 'farms': 58, 'woods': 15, 'tours': 74, 'cooperative': 58, 'skin': 50, 'fixtures': 86, 'adjustment': 51, 'religious': 65, 'centers': 64, 'votes': 56, 'graves': 66, 'fellowship': 64, 'segments': 67, 'monasteries': 66, 'periodicals': 31, 'gigs': 74, 'riders': 86, 'carnivals': 10, 'bays': 51, 'contours': 67, 'dirty': 89, 'include': 56, 'presentation': 57, 'meadows': 80, 'resources': 35, 'hill': 19, 'washroom': 25, 'activities': 68, 'labels': 33, 'premium': 58, 'recitals': 33, 'homes': 88, 'perishable': 72, 'bulletin': 64, 'railways': 76, 'retailers': 47, 'vegan': 72, 'cemeteries': 75, 'street': 19, 'cellular': 52, 'cook': 87, 'clearings': 38, 'precinct': 18, 'alpine': 68, 'recreation': 62, 'magic': 6, 'prize': 58, 'solutions': 35, 'yachting': 60, 'crops': 45, 'positions': 9, 'companies': 39, 'kiosks': 58, 'standards': 35, 'race': 76, 'Halal': 72, 'relics': 15, 'car': 50, 'radio': 83, 'hostels': 17, 'landlords': 77, 'ornamental': 39, 'spiritual': 3, 'neighborhood': 19, 'pledge': 58, 'core': 79, 'tea': 87, 'traveler': 35, 'cyber': 16, 'layouts': 43, 'titles': 21, 'carriages': 48, 'perspective': 78, 'pans': 89, 'licenses': 39, 'cloisters': 59, 'birdwatching': 81, 'scientific': 65, 'mausoleums': 59, 'swamps': 13, 'domestic': 69, 'public': 53, 'indian': 16, 'poles': 51, 'new': 87, 'net': 79, 'European': 69, 'plush': 39, 'lowlands': 80, 'transportation': 79, 'commercial': 53, 'ramps': 85, 'lakes': 70, 'water': 50, 'hubs': 47, 'tracks': 67, 'pickets': 63, 'bamboos': 89, 'aid': 56, 'LSTs': 63, 'canals': 89, 'steamships': 26, 'hoops': 86, 'bakeries': 61, 'biodiversity': 78, 'items': 82, 'vegetarian': 72, 'casino': 42, 'sustainability': 61, 'fortresses': 66, 'museums': 76, 'miniature': 39, 'airport': 32, 'base': 76, 'products': 79, 'social': 65, 'priceless': 3, 'weird': 21, 'anthropological': 88, 'rafting': 85, 'climber': 35, 'coastline': 54, 'lighthouses': 56, 'hilltops': 34, 'fantastic': 21, 'tasks': 68, 'addresses': 33, 'humour': 21, 'hedgerows': 7, 'transit': 79, 'precincts': 75, 'private': 82, 'bullock': 81, 'screens': 86, 'marvelous': 3, 'busses': 26, 'topographical': 88, 'refreshment': 25, 'cities': 78, 'residences': 75, 'ballets': 90, 'festivals': 33, 'woodland': 78, 'tools': 79, 'cloud': 78, 'hotels': 58, 'literary': 88, 'from': 56, 'sunbathing': 67, 'songs': 67, 'lockers': 49, 'two': 87, 'coffeehouses': 38, 'rustic': 39, 'leaks': 89, 'bike': 73, 'music': 6, 'archives': 23, 'characteristics': 43, 'scope': 78, 'chateaux': 59, 'markets': 77, 'more': 22, 'fragmentary': 3, 'walkways': 20, 'holy': 3, 'towers': 51, 'carvings': 0, 'waterways': 80, 'wildlife': 78, 'forests': 70, 'plantations': 45, 'campsites': 29, 'factories': 58, 'karaoke': 2, 'town': 32, 'organizations': 68, 'balls': 86, 'mythical': 15, 'allotments': 45, 'science': 6, 'inertial': 52, 'districts': 78, 'movies': 21, 'locker': 25, 'regions': 78, 'publications': 71, 'island': 32, 'ferry': 50, 'pickle': 19, 'choirs': 90, 'piers': 85, 'history': 56, 'crazy': 21, 'bogs': 40, 'hamburger': 19, 'speciality': 58, 'baronies': 75, 'galleries': 31, 'sentries': 63, 'sample': 79, 'skydiving': 60, 'minimum': 79, 'fanciful': 3, 'quartets': 90, 'woodlands': 70, 'sense': 78, 'databases': 71, 'intramural': 68, 'information': 56, 'educational': 88, 'backpacking': 85, 'worldview': 78, 'technology': 79, 'Concerning': 56, 'boxing': 83, 'ledges': 34, 'traders': 77, 'liveries': 43, 'hot': 89, 'townlands': 75, 'forest': 78, 'sacred': 82, 'beach': 19, 'taverns': 17, 'stock': 83, 'rinks': 10, 'poker': 37, 'regional': 69, 'ballroom': 14, 'hog': 19, 'farm': 47, 'mangroves': 40, 'communal': 68, 'lab': 18, 'entrepreneurship': 61, 'applications': 79, 'paintball': 81, 'district': 32, 'adventure': 57, 'records': 56, 'vases': 0, 'seashells': 89, 'authentic': 15, 'racks': 51, 'gorges': 34, 'lifesaving': 81, 'branches': 9, 'athletics': 83, 'commodity': 58, 'light': 79, 'conglomerates': 61, 'provinces': 36, 'lines': 67, 'volleyball': 37, 'tulip': 19, 'bakery': 42, 'civics': 61, 'truck': 73, 'villas': 84, 'banks': 78, 'rentals': 49, 'athletes': 86, 'bungee': 81, 'wine': 87, 'displays': 33, 'theme': 57, 'neighbourhoods': 56, 'concertos': 90, 'hierarchy': 64, 'lithographic': 39, 'astronomical': 88, 'thermal': 52, 'through': 56, 'costume': 6, 'condominiums': 29, 'bulldozers': 63, 'cold': 89, 'rocks': 54, 'journals': 71, 'industries': 77, 'bridges': 51, 'entrances': 85, 'gymnastic': 81, 'masses': 9, 'recreational': 68, 'racecar': 81, 'nostalgia': 21, 'isolation': 51, 'better': 22, 'trams': 26, 'permanent': 53, 'dwellings': 75, 'savory': 72, 'hobby': 58, 'soccer': 37, 'parades': 74, 'artisanal': 39, 'coffee': 87, 'geysers': 89, 'food': 87, 'practice': 23, 'nation': 76, 'shuttle': 50, 'walls': 51, 'safari': 25, 'hands': 56, 'flea': 19, 'clouds': 89, 'oratorios': 90, 'airports': 77, 'greenhouses': 38, 'agro': 16, 'fundraisers': 10, 'grasslands': 70, 'kayaking': 85, 'sailor': 35, 'swimsuit': 2, 'fairs': 31, 'courses': 37, 'picnics': 17, 'lingerie': 2, 'lofts': 49, 'paddling': 67, 'pools': 86, 'entirely': 22, 'cliffs': 34, 'manors': 75, 'concerts': 33, 'volcanos': 41, 'bicycle': 73, 'schemes': 64, 'From': 56, 'busts': 0, 'fish': 87, 'prawn': 19, 'polychrome': 39, 'society': 23, 'overpasses': 26, 'dubstep': 2, 'corporations': 77, 'laboratory': 18, 'teams': 86, 'amusement': 29, 'projections': 67, 'initiatives': 68, 'marketplaces': 61, 'alcohol': 87, 'entertainment': 83, 'catacombs': 15, 'boutique': 58, 'factory': 47, 'hydraulic': 52, 'adhesion': 51, 'participants': 86, 'playground': 14, 'girders': 51, 'induction': 51, 'brewery': 47, 'shows': 33, 'foundation': 18, 'eco': 16, 'closings': 49, 'merchants': 77, 'waterfalls': 34, 'waterbirds': 38, 'depots': 45, 'labs': 71, 'houses': 88, 'snooker': 37, 'basketball': 37, 'campgrounds': 29, 'birding': 81, 'mudflats': 7, 'uplands': 13, 'scary': 21, 'dormitories': 17, 'milestones': 10, 'benefits': 35, 'equine': 16, 'shelves': 85, 'habitats': 70, 'miners': 77, 'modules': 83, 'ministries': 64, 'plane': 50, 'palaces': 75, 'reels': 51, 'rainforest': 78, 'synagogues': 59, 'picnicking': 81, 'initial': 79, 'features': 33, 'ethical': 3, 'attractions': 76, 'softball': 37, 'bazaars': 61, 'wash': 87, 'philosophical': 65, 'establishments': 47, 'agri': 16, 'abutments': 20, 'inns': 17, 'cups': 86, 'temples': 59, 'city': 76, 'story': 57, 'ancient': 15, 'publication': 23, 'service': 23, 'festival': 64, 'grilles': 51, 'influence': 56, 'engagement': 51, 'traveller': 35, 'rails': 85, 'hollows': 7, 'boating': 85, 'philanthropy': 61, 'conservation': 79, 'parasailing': 60, 'trails': 85, 'structures': 88, 'store': 47, 'interests': 68, 'lottery': 64, 'releases': 67, 'watersports': 62, 'academy': 18, 'gym': 42, 'hotel': 42, 'motorcycle': 73, 'tombstones': 15, 'environmental': 65, 'optical': 52, 'rickshaw': 81, 'spas': 61, 'albums': 21, 'flowers': 54, 'ecotourism': 62, 'gambler': 35, 'viaducts': 20, 'pillboxes': 89, 'cracks': 89, 'sculptures': 0, 'hammocks': 38, 'boring': 21, 'volcanoes': 40, 'dikes': 40, 'youth': 83, 'headlands': 34, 'fabulous': 3, 'historical': 82, 'trekking': 85, 'fishermen': 77, 'chalets': 61, 'scuba': 81, 'spurs': 89, 'interactive': 68, 'and': 56, 'bridge': 19, 'topics': 82, 'modern': 15, 'locations': 88, 'buildings': 88, 'raw': 89, 'childcare': 61, 'halal': 72, 'stalls': 86, 'breakfast': 29, 'organs': 83, 'seminar': 64, 'paths': 67, 'constructions': 83, 'handicraft': 14, 'cottages': 84, 'shorts': 21, 'subdivisions': 56, 'parks': 76, 'dining': 29, 'rehearsals': 33, 'subjects': 82, 'luxury': 58, 'doors': 67, 'transnational': 16, 'tunnels': 89, 'jungle': 78, 'villages': 54, 'multiple': 87, 'equestrian': 68, 'theatre': 6, 'centre': 18, 'singles': 21, 'cathedrals': 59, 'sets': 56, 'troughs': 40, 'complexes': 83, 'intergalactic': 16, 'lists': 33, 'convents': 59, 'engagements': 74, 'sinkholes': 89, 'artefacts': 0, 'observation': 51, 'neighborhoods': 80, 'lessons': 37, 'boardwalks': 20, 'performances': 33, 'coves': 34, 'snowmobiling': 81, 'bookstore': 42, 'artistic': 88, 'mechanical': 52, 'brew': 87, 'professional': 69, 'salt': 50, 'institutions': 68, 'goals': 56, 'sector': 18, 'reefs': 40, 'hiking': 85, 'golf': 37, 'cruises': 74, 'formal': 82, 'indoor': 68, 'sites': 82, 'bookings': 49, 'colors': 67, 'session': 64, 'businesses': 77, 'shoe': 58, 'midwife': 35, 'cabins': 51, 'boutiques': 58, 'networks': 79, 'ground': 50, 'toast': 87, 'knowledge': 56, 'peasants': 77, 'basilicas': 59, 'ruin': 15, 'striptease': 2, 'sugar': 87, 'only': 22, 'rice': 87, 'local': 82, 'cockpits': 51, 'shepherd': 35, 'monuments': 84, 'canyons': 34, 'sights': 43, 'secular': 3, 'railings': 20, 'dry': 89, 'maritime': 16, 'fortifications': 66, 'minarets': 34, 'churches': 88, 'breakbeat': 2, 'leases': 39, 'botanical': 88, 'requirement': 64, 'areas': 82, 'tobacco': 87, 'wellness': 61, 'workman': 35, 'performers': 86, 'nutritious': 72, 'alteration': 51, 'marinas': 29, 'perfume': 87, 'sacrifices': 15, 'monumental': 82, 'architecture': 6, 'activity': 68, 'murals': 84, 'ruins': 15, 'vision': 78, 'restaurants': 58, 'lettering': 86, 'bars': 86, 'official': 69, 'art': 6, 'concert': 64, 'psychological': 65, 'national': 69, 'fable': 57, 'startup': 58, 'emergent': 15, 'culture': 23, 'electrostatic': 52, 'sparkling': 89, 'changes': 56, 'parking': 29, 'sport': 83, 'SCUBA': 81, 'points': 56, 'seminaries': 59, 'cosplay': 2, 'camping': 85, 'farmers': 77, 'pictures': 67, 'swimwear': 2, 'hatcheries': 38, 'libraries': 71, 'premises': 88, 'state': 76, 'future': 87, 'various': 87, 'furnishings': 84, 'conceptual': 88, 'sanctuaries': 75, 'caves': 80, 'numerous': 87, 'decks': 51, 'corridors': 85, 'carbonated': 72, 'infrastructure': 79, 'pedagogical': 88, 'enclosures': 85, 'nature': 78, 'importance': 56, 'franchises': 86, 'volumetric': 52, 'souvenir': 58, 'offices': 88, 'affiliates': 47, 'premise': 57, 'systems': 79, 'angling': 14, 'imprompt': 68, 'regular': 53, 'rodeos': 10, 'mariner': 35, 'congregations': 59, 'sanitation': 79, 'restaurant': 47, 'country': 76, 'cafes': 61, 'reliefs': 0, 'presentations': 37, 'trips': 74, 'kosher': 72, 'players': 86, 'kitchens': 84, 'figures': 9, 'auctions': 49, 'midwifery': 61, 'searchlights': 63, 'statues': 15, 'fields': 78, 'ranchers': 77, 'basins': 13, 'snowshoeing': 81, 'trackways': 89, 'caverns': 7, 'venues': 10, 'ballparks': 10, 'church': 19, 'springs': 89, 'regenerative': 52, 'boat': 50, 'bingo': 37, 'arts': 6, 'packages': 39, 'cycling': 83, 'motorbike': 73, 'icebergs': 89, 'union': 76, 'dams': 48, 'political': 65, 'three': 87, 'chimneys': 20, 'suburbs': 28, 'secret': 53, 'viticulture': 14, 'maintenance': 79, 'basic': 53, 'linguistic': 65, 'fry': 87, 'exhibition': 57, 'cutouts': 43, 'placenames': 56, 'life': 23, 'tournament': 64, 'shopping': 29, 'counselling': 61, 'sectors': 77, 'blessing': 58, 'enterprises': 77, 'convention': 64, 'orchestras': 33, 'vents': 89, 'standup': 2, 'cantatas': 90, 'towns': 36, 'sticky': 89, 'spirit': 78, 'locales': 56, 'divisions': 9, 'arias': 90, 'atmospheric': 52, 'adaptations': 43, 'stadia': 10, 'frozen': 89, 'tribal': 69, 'entrepreneurial': 16, 'programme': 64, 'policies': 68, 'fun': 21, 'curricula': 37, 'shops': 58, 'biking': 85, 'dykes': 7, 'vaults': 51, 'lodges': 76, 'aquaria': 38, 'playgrounds': 17, 'canoeing': 85, 'canoe': 50, 'almost': 22, 'soil': 50, 'spectacle': 57, 'workplaces': 38, 'surface': 50, 'refinery': 47, 'soils': 70, 'arrangements': 37, 'malls': 76, 'baths': 84, 'arenas': 10, 'restroom': 25, 'musicals': 33, 'movements': 9, 'blockhouses': 63, 'different': 87, 'grandiose': 3, 'dairies': 61, 'marshlands': 7, 'stadiums': 86, 'vintage': 39, 'landmarks': 56, 'parishes': 59, 'jogging': 85, 'scooter': 73, 'matches': 56, 'periodic': 79, 'sidecar': 73, 'regattas': 10, 'units': 9, 'games': 21, 'colonies': 36, 'events': 68, 'sled': 73, 'development': 56, 'oil': 87, 'temporary': 53, 'fraternity': 64, 'assignment': 64, 'drink': 87, 'parkways': 56, 'opulent': 39, 'cafeterias': 17, 'pubs': 29, 'wrestling': 83, 'levels': 56, 'architectures': 83, 'rockabilly': 2, 'cityscape': 14, 'tuna': 19, 'magician': 35, 'residents': 28, 'lacrosse': 37, 'noodle': 19, 'theater': 42, 'scenario': 78, 'programs': 68, 'navigation': 79, 'cultural': 65, 'motorcycling': 60, 'materials': 79, 'components': 79, 'centres': 82, 'theatres': 33, 'traffic': 79, 'laboratories': 71, 'corporate': 16, 'investments': 35, 'bodies': 9, 'scholarship': 64, 'seasonal': 68, 'gates': 51, 'outdoor': 68, 'stores': 39, 'livestock': 78, 'just': 22, 'less': 22, 'barbecues': 49, 'embankments': 20, 'biodegradable': 72, 'restrooms': 17, 'communities': 78, 'madrigals': 90, 'cays': 89, 'provincial': 69, 'seats': 56, 'tone': 78, 'startups': 47, 'stairways': 20, 'assemblages': 83, 'hills': 80, 'localities': 28, 'watchtowers': 89, 'residential': 82, 'shrines': 0, 'international': 69, 'bookshops': 38, 'location': 23, 'wet': 89, 'openings': 67, 'transformation': 51, 'eateries': 61, 'government': 76, 'docks': 48, 'Chinatown': 14, 'architectural': 88, 'warehouse': 47, 'boxes': 86, 'historic': 82, 'five': 87, 'community': 32, 'barge': 50, 'performance': 23, 'castings': 43, 'world': 76, 'execution': 51, 'projects': 82, 'meat': 87, 'sightseeing': 62, 'county': 32, 'clam': 19, 'mansions': 66, 'ramparts': 20, 'schools': 88, 'concerti': 90, 'gyms': 10, 'miracle': 58, 'intercollegiate': 68, 'physiotherapy': 61, 'zoos': 38, 'wineries': 31, 'vegetation': 78, 'Chinatowns': 38, 'paragliding': 81, 'soft': 89, 'directories': 71, 'imprints': 43, 'names': 33, 'classes': 37, 'valleys': 80, 'shuttles': 26, 'village': 32, 'magnificent': 82, 'competition': 21, 'platforms': 67, 'clubs': 86, 'productions': 74, 'ornaments': 0, 'images': 67, 'contests': 10, 'bindings': 43, 'transport': 79, 'chorus': 57, 'humor': 21, 'for': 56, 'dunes': 89, 'colonial': 15, 'legal': 3, 'passageways': 7, 'competitions': 86, 'tramways': 26, 'dealership': 47, 'sledding': 81, 'pattern': 79, 'panes': 51, 'conference': 64, 'recyclable': 72, 'medieval': 82, 'prairies': 80, 'terraces': 85, 'bathhouses': 61, 'outlets': 47, 'stew': 87, 'lounges': 49, 'crap': 21, 'pumps': 89, 'properties': 82, 'beaches': 80, 'gears': 51, 'picnic': 29, 'actual': 15, 'boards': 64, 'of': 56, 'newspapers': 31, 'lookouts': 63, 'nightclub': 42, 'dinner': 29, 'involving': 56, 'economic': 65, 'corals': 40, 'islands': 70, 'concession': 58, 'homesteads': 75, 'windsurfing': 81, 'road': 19, 'pollution': 79, 'antique': 39, 'primitive': 15, 'memorials': 0, 'wilderness': 78, 'interruption': 51, 'whites': 77, 'landowners': 77, 'vacation': 29, 'fishes': 40, 'stalactites': 89, 'jet': 73, 'roads': 88, 'episodes': 67, 'lesson': 58, 'sports': 83, 'revues': 90, 'steamboats': 63, 'canteens': 17, 'infrastructures': 77, 'grids': 83, 'shires': 59, 'area': 32, 'grapevine': 19, 'museum': 18, 'tennis': 37, 'fundraiser': 64, 'gift': 58, 'fast': 89, 'custom': 58, 'parachute': 81, 'workshop': 18, 'abbeys': 59, 'stars': 67, 'amenities': 76, 'leagues': 86, 'mountains': 70, 'Regarding': 56, 'medium': 79, 'interest': 56, 'SeaWorld': 62, 'capability': 79, 'volunteerism': 61, 'workshops': 37, 'specialty': 58, 'fountains': 84, 'slums': 28, 'cores': 83, 'fisheries': 78, 'archaic': 15, 'sardine': 19, 'staircases': 20, 'library': 18, 'crane': 50, 'calico': 39, 'shutters': 51, 'patriot': 35, 'dowry': 58, 'comics': 6, 'breweries': 31, 'artisans': 77, 'authority': 56, 'clips': 67, 'carriage': 50, 'sponsorships': 49, 'nightlife': 25, 'winery': 42, 'casts': 33, 'flats': 45, 'panels': 83, 'landscapes': 84, 'circuses': 38, 'Townsville': 62, 'castles': 75, 'rapids': 80, 'wellbeing': 61, 'circus': 19, 'urns': 0, 'covers': 33, 'evidence': 56, 'reservoirs': 48, 'mountaineering': 30, 'field': 76, 'ship': 50, 'cafe': 42, 'yearbook': 64, 'dealer': 47, 'shit': 21, 'programmes': 37, 'bicycling': 85, 'storage': 79, 'aquariums': 38, 'application': 56, 'other': 87, 'electrical': 52, 'snorkeling': 81, 'tugboats': 63, 'department': 18, 'depot': 47, 'smell': 87, 'potential': 79, 'revision': 78, 'hillsides': 80, 'suites': 37, 'operettas': 90, 'congress': 64, 'theatrical': 88, 'ravines': 7, 'narrative': 57, 'utilities': 77, 'diet': 87, 'apparel': 83, 'ecological': 65, 'midget': 73, 'pathways': 83, 'marshes': 13, 'ferries': 48, 'brands': 39, 'depicting': 56, 'stocks': 39, 'strips': 43, 'seamounts': 89, 'land': 50, 'assets': 35, 'amusements': 25, 'forts': 66, 'foundry': 47, 'departments': 64, 'stacks': 51, 'beds': 45, 'hikes': 49, 'beverage': 87, 'mass': 79, 'rallies': 74, 'orphanages': 38, 'rural': 82, 'banners': 86, 'Oah': 62, 'mosaics': 0, 'gardens': 84, 'once': 22}

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
  
def check_all_distance(query, sets):
  out = query.translate(string.punctuation)
  out = out.lower()
  words = out.split()
  
  result = []
  
  for w in words:
    if (w in sets):
      result.append(w)
    else:
      for l in sets:
        if (levenshteinDistance(w,l) < 3):
          result.append(l)
          break
          
  return result
  

def get_category(syn_array):
  result = []
  for i in syn_array:
    result.append(categories[syns_to_cat[i]])

  return list(set(result))

	
def query_expansion(query):
  pars = query.split('&')
  #place
  place = check_all_distance(pars[0].replace('place=',''), locations)
  if (not place):
    place = ''
  else:
    place = place[0]

  #categories
  category = get_category(check_all_distance(pars[1].replace('categories=','').replace('+', ' '), syns))
  open_time = pars[2].replace('from=','')
  close_time = pars[3].replace('until=','')
  return (place, category, open_time, close_time)

#(p, c, o, cl) = query_expansion('place=jakata&categories=shoppin&from=&until=')