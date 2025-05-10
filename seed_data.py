import json
from database import init_db, add_knowledge, get_db_connection

def seed():
    """Populates the database with initial Hikkaduwa information."""
    print("Seeding database...")
    init_db() # Ensure tables exist

    # Clear existing data
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM knowledge")
    conn.commit()
    conn.close()

    # Add Sample Hotel Data
    add_knowledge(
        category='hotel',
        name='Hikka Tranz by Cinnamon',
        description='Popular beachfront hotel with vibrant atmosphere and modern amenities.',
        details=json.dumps(dict(Address='Galle Rd, Hikkaduwa.', Features='Pool, Restaurants, Bars, Beach Access, Spa.', Average_Price='$140 per night.')),
        relevance=5
    )
    add_knowledge(
        category='hotel',
        name='Citrus Hikkaduwa',
        description='Lively beachfront hotel with comfortable rooms and a range of dining options.',
        details=json.dumps(dict(Address='Hikkaduwa Beach, Hikkaduwa.', Features='Outdoor Pool, Restaurants, Bars, Beach Access, Spa.', Average_Price='$88 per night.')),
        relevance=5
    )
    add_knowledge(
        category='hotel',
        name='Riff Hikkaduwa',
        description='Stylish beachfront hotel with contemporary design and excellent facilities.',
        details=json.dumps(dict(Address='Hikkaduwa Beach, Hikkaduwa.', Features='Infinity Pool, Rooftop Bar, Restaurants, Spa, Fitness Center, Beach Access.', Average_Price='$141 per night.')),
        relevance=5
    )
    add_knowledge(
        category='hotel',
        name='Roman Beach Hotel',
        description='Boutique beachfront hotel offering spacious rooms with sea views and a tranquil ambiance.',
        details=json.dumps(dict(Address='777/2 Galle Road, Thiranagama, Hikkaduwa.', Features='Outdoor Pool, Private Beachfront, Restaurant, Bar, Free Wi-Fi.', Average_Price='$171 per night.')),
        relevance=3
    )
    add_knowledge(
        category='hotel',
        name='Coral Sands Hotel',
        description='Beachfront hotel with comfortable accommodations and a swimming pool.',
        details=json.dumps(dict(Address='Hikkaduwa Beach, Hikkaduwa.', Features='Pool, Restaurant, Bar, Beach Access, Spa.', Average_Price='$63 per night.')),
        relevance=3
    )
    add_knowledge(
        category='hotel',
        name='Amaroo Hikkaduwa',
        description='Charming hotel located near Narigama beach with comfortable rooms and a restaurant.',
        details=json.dumps(dict(Address='Hikkaduwa, 90 metres from Narigama beach.', Features='Garden, Free Private Parking, Terrace, Restaurant, Beach Access.', Average_Price='$39 per night.')),
        relevance=3
    )
    add_knowledge(
        category='hotel',
        name='Hikka Sandy Pearl Beach Resort',
        description='Relaxed beachfront hotel featuring an infinity pool and a restaurant with a bar.',
        details=json.dumps(dict(Address='No.370 Galle Rd, Hikkaduwa.', Features='Infinity Pool, Restaurant, Bar, Sandy Terrace, Beach Access.', Average_Price='$29 per night.')),
        relevance=3
    )
    add_knowledge(
        category='hotel',
        name='DORMERO Hotel Sri Lanka Hikkaduwa Beach',
        description='Modern beachfront hotel with excellent facilities and a focus on guest comfort.',
        details=json.dumps(dict(Address='Hikkaduwa Beach, Hikkaduwa.', Features='Outdoor Pool, Fitness Center, Garden, Restaurant, Bar, Beach Access.', Average_Price='$214 per night.')),
        relevance=2
    )
    add_knowledge(
        category='hotel',
        name='Plantation House',
        description='Beautiful hotel with a garden and bar, offering comfortable and spacious rooms.',
        details=json.dumps(dict(Address='Hikkaduwa, 2.5 km from Hikkaduwa Coral Reef.', Features='Garden, Bar, Free Wi-Fi, Pool.', Average_Price='Information not readily available.')),
        relevance=2
    )
    add_knowledge(
        category='hotel',
        name='Hikkaduwa Beach Hotel',
        description='Well-established beachfront hotel with direct access to the beach and various amenities.',
        details=json.dumps(dict(Address='298 Galle Rd, Hikkaduwa.', Features='Outdoor Pool, Restaurant, Bar, Beach Access.', Average_Price='$56 per night.')),
        relevance=2
    )
    # Add Sample Activity Data
    add_knowledge(
        category='activity',
        name='Surfing',
        description='Hikkaduwa is famous for surfing, with spots suitable for beginners and experienced surfers.',
        details=json.dumps(dict(Best_Season='November to April.', note='Main surf points near the main beach and Narigama.')),
        relevance=5
    )
    add_knowledge(
        category='activity',
        name='Snorkeling and Coral Reef Exploration',
        description='Discover the vibrant coral reefs and diverse marine life just offshore.',
        details=json.dumps(dict(Best_Spots='Hikkaduwa Coral Sanctuary.', note='Equipment can be rented from local shops.')),
        relevance=5
    )
    add_knowledge(
        category='activity',
        name='Scuba Diving',
        description='Explore deeper underwater sites, including shipwrecks and colorful coral gardens.',
        details=json.dumps(dict(note='Numerous dive centers offer courses and guided dives for all levels.')),
        relevance=5
    )
    add_knowledge(
        category='activity',
        name='Glass Bottom Boat Ride',
        description='Enjoy the beauty of the coral reefs and fish without getting wet.',
        details=json.dumps(dict(note='Boats available near the main beach area, offering tours of varying durations.')),
        relevance=3
    )
    add_knowledge(
        category='activity',
        name='Visit the Tsunami Memorial',
        description='Reflect at the poignant memorial dedicated to the victims of the 2004 tsunami.',
        details=json.dumps(dict(note='Located along the Galle Road, a place for quiet contemplation.')),
        relevance=2
    )
    add_knowledge(
        category='activity',
        name='Relaxing on the Beach',
        description='Unwind on the golden sands, soak up the sun, and enjoy the ocean breeze.',
        details=json.dumps(dict(note='Popular beaches include Hikkaduwa Beach and Narigama Beach.')),
        relevance=5
    )
    add_knowledge(
        category='activity',
        name='Sea Turtle Hatchery Visit',
        description='Learn about sea turtle conservation efforts and witness baby turtles (seasonal).',
        details=json.dumps(dict(note='Several hatcheries located near Hikkaduwa, supporting turtle rescue and release.')),
        relevance=3
    )
    add_knowledge(
        category='activity',
        name='Lagoon Boat Trip',
        description='Take a scenic boat ride through the Hikkaduwa lagoon, observing mangroves and birdlife.',
        details=json.dumps(dict(note='Boat tours often include visits to Cinnamon Island and local fish spas.')),
        relevance=3
    )
    add_knowledge(
        category='activity',
        name='Shopping for Souvenirs',
        description='Browse the local shops and stalls for handicrafts, jewelry, clothing, and spices.',
        details=json.dumps(dict(note='Shops are located along the Galle Road and in the main town area.')),
        relevance=2
    )
    add_knowledge(
        category='activity',
        name='Enjoying Seafood',
        description='Savor fresh and delicious seafood at the numerous restaurants along the coast.',
        details=json.dumps(dict(note='Many restaurants offer a variety of grilled, curried, and fried seafood dishes.')),
        relevance=3
    )

    # Add Sample Getting around Data
    add_knowledge(
        category='getting_around',
        name='Tuk-Tuks (Three-Wheelers)',
        description='A common and convenient way for short distances within Hikkaduwa.',
        details=json.dumps(dict(note='Negotiate the fare before starting your journey. Ideal for quick trips around town and to nearby beaches.')),
        relevance=5
    )

    add_knowledge(
        category='getting_around',
        name='Scooters/Motorbikes',
        description='Offers flexibility for exploring Hikkaduwa and surrounding areas at your own pace.',
        details=json.dumps(dict(note='Available for rent from various local shops. Ensure you have a valid license and wear a helmet. Be cautious of local traffic.')),
        relevance=5
    )

    add_knowledge(
        category='getting_around',
        name='Bicycles',
        description='A budget-friendly and eco-friendly option for shorter distances.',
        details=json.dumps(dict(note='Can be rented from some guesthouses and shops. Suitable for leisurely rides along the coast road.')),
        relevance=3
    )

    add_knowledge(
        category='getting_around',
        name='Local Buses',
        description='A very affordable option for traveling longer distances along the main Galle Road.',
        details=json.dumps(dict(note='Buses can be crowded and may not have air conditioning. Useful for reaching nearby towns like Galle or Ambalangoda.')),
        relevance=2
    )

    add_knowledge(
        category='getting_around',
        name='Taxi Services',
        description='More comfortable option for longer distances or when traveling with luggage.',
        details=json.dumps(dict(note='Can be arranged through hotels or local taxi stands. Fares are generally higher than tuk-tuks or buses.')),
        relevance=2
    )

    # Add Sample Local food Data
    add_knowledge(
        category='local_food',
        name='Seafood (Grilled/Curried)',
        description='Freshly caught seafood is a highlight, often grilled or prepared in flavorful Sri Lankan curries.',
        details=json.dumps(dict(note='Popular options include fish, prawns, crab, and lobster. Many restaurants along the beach offer daily catches.')),
        relevance=5
    )

    add_knowledge(
        category='local_food',
        name='Rice and Curry',
        description='A staple Sri Lankan dish with a variety of vegetable, meat, or fish curries served with rice.',
        details=json.dumps(dict(note='Each restaurant offers its own unique selection of curries. Try different variations to experience the local flavors.')),
        relevance=5
    )

    add_knowledge(
        category='local_food',
        name='Hoppers (Appa)',
        description='Bowl-shaped pancakes made from rice flour and coconut milk, often served with eggs or savory fillings.',
        details=json.dumps(dict(note='A popular breakfast or snack item, widely available from street vendors and local eateries.')),
        relevance=4
    )

    add_knowledge(
        category='local_food',
        name='Kottu Roti',
        description='A Sri Lankan street food made by chopping up roti (flatbread) and mixing it with vegetables, eggs, and/or meat.',
        details=json.dumps(dict(note='A flavorful and filling dish, often prepared with various spices. You can usually customize the ingredients.')),
        relevance=4
    )

    add_knowledge(
        category='local_food',
        name='Roti (Godamba Roti)',
        description='Flatbreads that can be eaten plain or filled with sweet or savory ingredients.',
        details=json.dumps(dict(note='Popular fillings include coconut (pol roti), vegetables, or cheese.')),
        relevance=3
    )

    add_knowledge(
        category='local_food',
        name='String Hoppers (Idiyappam)',
        description='Steamed noodles made from rice flour, often eaten with curries or coconut milk.',
        details=json.dumps(dict(note='A light and easily digestible dish, commonly served for breakfast or dinner.')),
        relevance=3
    )

    add_knowledge(
        category='local_food',
        name='Watalappan',
        description='A rich and creamy coconut custard sweetened with jaggery (palm sugar) and spiced with cardamom and nutmeg.',
        details=json.dumps(dict(note='A traditional Sri Lankan dessert, often served at special occasions but also available in restaurants.')),
        relevance=3
    )

    # Add Sample surfing spots Data
    add_knowledge(
        category='surfing_spots',
        name='Main Reef Break (Hikkaduwa Point)',
        description='A popular right-hand reef break suitable for intermediate to advanced surfers.',
        details=json.dumps(dict(note='Consistent waves during the surfing season (November to April). Can get crowded.')),
        relevance=5
    )

    add_knowledge(
        category='surfing_spots',
        name="Benny's (North of Hikkaduwa Point)",
        description = 'A left-hand reef break, generally a bit mellower than the main point.',
        details =json.dumps(dict(note='Good for intermediate surfers. Can also have some fun smaller days.')),
        relevance = 4
    )

    add_knowledge(
        category='surfing_spots',
        name='Narigama Beach Breaks',
        description='Offers a variety of beach breaks suitable for beginners and longboarders.',
        details=json.dumps(dict(note='More forgiving waves compared to the reef breaks. Plenty of space to learn.')),
        relevance=4
    )

    add_knowledge(
        category='surfing_spots',
        name='North Jetty (near the harbor)',
        description='A right-hand wave that can be fun on its day.',
        details=json.dumps(dict(note="Less consistent than the main point but can offer good rides when it's working.")),
        relevance=3
    )

    # Add Sample snorkeling diving Data
    add_knowledge(
        category='snorkeling_diving',
        name='Hikkaduwa Coral Sanctuary',
        description='Shallow reef area easily accessible from the beach, perfect for snorkeling.',
        details=json.dumps(dict(note='See colorful corals, various fish species, and sometimes turtles. Be mindful not to step on the coral.')),
        relevance=5
    )

    add_knowledge(
        category='snorkeling_diving',
        name='Coral Gardens (further offshore)',
        description='Deeper sections of the reef offering more diverse marine life for both snorkeling and diving.',
        details=json.dumps(dict(note='Boat trips are available to reach these areas. Expect to see larger fish and more intricate coral formations.')),
        relevance=4
    )

    add_knowledge(
        category='snorkeling_diving',
        name='Wreck Dives (e.g., Earl of Shaftesbury)',
        description='Several shipwrecks in the area offer unique diving experiences.',
        details=json.dumps(dict(note='Suitable for certified divers. Explore historical wrecks and the marine life that has made them home.')),
        relevance=3
    )

    add_knowledge(
        category='snorkeling_diving',
        name='Rock Formations and Reef Patches (south of the main reef)',
        description='Various underwater rock structures and smaller reef patches offer interesting snorkeling and diving opportunities.',
        details=json.dumps(dict(note='Explore different underwater landscapes and encounter a variety of marine creatures.')),
        relevance=3
    )

    # Add Sample safety tips Data

    add_knowledge(
        category='safety_tips',
        name='Swim within designated safe areas and be aware of currents.',
        description='The ocean can have strong currents, especially near reef breaks.',
        details=json.dumps(dict(note='Look for flags indicating safe swimming zones and ask locals for advice.')),
        relevance=5
    )

    add_knowledge(
        category='safety_tips',
        name='Be cautious of tuk-tuk drivers and negotiate fares beforehand.',
        description='While most drivers are honest, overcharging can occur.',
        details=json.dumps(dict(note='Agree on a price before starting your journey or use ride-hailing apps if available.')),
        relevance=4
    )

    add_knowledge(
        category='safety_tips',
        name='Protect yourself from the sun with sunscreen, hats, and sunglasses.',
        description='The tropical sun can be intense, even on cloudy days.',
        details=json.dumps(dict(note='Apply high SPF sunscreen regularly and stay hydrated.')),
        relevance=5
    )

    add_knowledge(
        category='safety_tips',
        name='Be aware of your belongings and avoid leaving valuables unattended.',
        description='Petty theft can occur in tourist areas.',
        details=json.dumps(dict(note='Keep your belongings secure and consider using hotel safes.')),
        relevance=4
    )

    add_knowledge(
        category='safety_tips',
        name='Stay hydrated by drinking plenty of bottled water.',
        description='Tap water is generally not recommended for drinking.',
        details=json.dumps(dict(note='Carry a reusable water bottle and refill it with purchased bottled water.')),
        relevance=5
    )

    add_knowledge(
        category='safety_tips',
        name='Be respectful of local customs and traditions.',
        description='Sri Lanka has a rich cultural heritage.',
        details=json.dumps(dict(note='Dress modestly when visiting religious sites and ask for permission before taking photos of people.')),
        relevance=3
    )

    add_knowledge(
        category='safety_tips',
        name='Be cautious of stray animals, especially dogs.',
        description='While many are harmless, some may be unpredictable.',
        details=json.dumps(dict(note='Avoid approaching or feeding stray animals.')),
        relevance=3
    )

    # Add Sample Budget Travel Data
    add_knowledge(
        category='budget_travel',
        name='Stay in guesthouses or budget-friendly hotels.',
        description='Numerous affordable accommodations are available away from the main beachfront resorts.',
        details=json.dumps(dict(note='Look for options slightly inland or on the southern end of Narigama beach for better deals.')),
        relevance=5
    )

    add_knowledge(
        category='budget_travel',
        name='Eat at local "roti shops" and street food stalls.',
        description='Delicious and inexpensive local food options are widely available.',
        details=json.dumps(dict(note='Enjoy kottu roti, vegetable roti, and other local snacks at very reasonable prices.')),
        relevance=5
    )

    add_knowledge(
        category='budget_travel',
        name='Use local buses for longer journeys.',
        description='The most cost-effective way to travel between towns.',
        details=json.dumps(dict(note='Be prepared for crowded conditions but enjoy the local experience.')),
        relevance=4
    )

    add_knowledge(
        category='budget_travel',
        name='Rent a bicycle for local exploration.',
        description='A cheap and healthy way to get around Hikkaduwa.',
        details=json.dumps(dict(note='Negotiate the rental price for longer durations.')),
        relevance=4
    )

    add_knowledge(
        category='budget_travel',
        name='Take advantage of free activities like swimming and sunbathing on the beach.',
        description='Enjoy the natural beauty of Hikkaduwa without spending money.',
        details=json.dumps(dict(note='Many beaches are public and offer a great way to relax.')),
        relevance=5
    )

    add_knowledge(
        category='budget_travel',
        name='Negotiate prices for tuk-tuks and in local markets.',
        description="Don't be afraid to haggle respectfully to get a fair price.",
        details=json.dumps(dict(note='Ask locals for a reasonable price range before negotiating.')),
        relevance=4
    )

    add_knowledge(
        category='budget_travel',
        name='Travel during the shoulder seasons (April-June, September-October).',
        description='You may find lower prices for accommodation and fewer crowds.',
        details=json.dumps(dict(note='Be aware that the weather might be more unpredictable during these periods.')),
        relevance=3
    )

    # Add Sample weather Data
    add_knowledge(
        category='weather',
        description='Hikkaduwa has a tropical climate. The main tourist season (dry) is typically from November to April. The monsoon season is usually May to October, but showers can occur anytime.',
        details=json.dumps(dict(note=f'Today is {datetime.now().strftime("%Y-%m-%d")}. For a current forecast, please check a reliable weather website.')),
        relevance=5
    )

    # Add Sample generic Data
    add_knowledge(
        category='general_info',
        description='Hikkaduwa is a coastal town in southwestern Sri Lanka, known for its beaches, coral reefs, and nightlife.',
        details=json.dumps(dict(note='Located about 100km south of Colombo.')),
        relevance=5
    )

    print("Database seeding complete.")

if __name__ == '__main__':
    from datetime import datetime # Import here for the seeding script
    seed()