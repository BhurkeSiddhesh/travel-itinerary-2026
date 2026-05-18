import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Headers
html = html.replace('Coorg · Mysuru · Ooty - May 2026', 'Coorg · Nagarhole Safari · Ooty — May 2026')
html = html.replace('<div class="mobile-brand">Coorg · Mysuru · Ooty</div>', '<div class="mobile-brand">Coorg · Nagarhole Safari · Ooty</div>')
html = html.replace('<div class="trip-name">Coorg · Mysuru<br>Ooty Circuit</div>', '<div class="trip-name">Coorg · Nagarhole Safari<br>Ooty Circuit</div>')

# 2. Update Sidebar
sidebar_old = """      <a href="#day4" class="nav-link">
        <span class="day-num">4</span>
        <div class="nav-text">
          <strong>Saturday, May 23</strong>
          <span>Mysuru</span>
        </div>
      </a>
      <a href="#day5" class="nav-link">
        <span class="day-num">5</span>
        <div class="nav-text">
          <strong>Sunday, May 24</strong>
          <span>Mysuru Full Day</span>
        </div>
      </a>
      <a href="#day6" class="nav-link">
        <span class="day-num">6</span>
        <div class="nav-text">
          <strong>Monday, May 25</strong>
          <span>Transit to Ooty</span>
        </div>
      </a>"""

sidebar_new = """      <a href="#day4" class="nav-link">
        <span class="day-num">4</span>
        <div class="nav-text">
          <strong>Saturday, May 23</strong>
          <span>Nagarhole Safari</span>
        </div>
      </a>
      <a href="#day5" class="nav-link">
        <span class="day-num">5</span>
        <div class="nav-text">
          <strong>Sunday, May 24</strong>
          <span>Nagarhole → Ooty</span>
        </div>
      </a>
      <a href="#day6" class="nav-link">
        <span class="day-num">6</span>
        <div class="nav-text">
          <strong>Monday, May 25</strong>
          <span>Ooty Full Day</span>
        </div>
      </a>"""
html = html.replace(sidebar_old, sidebar_new)

# 3. Update Route Map summary
route_old = """        <div class="circuit-route">
          <span class="circuit-stop">Mumbai</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Coorg</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Mysuru</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Ooty</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Mumbai</span>
        </div>"""
route_new = """        <div class="circuit-route">
          <span class="circuit-stop">Mumbai</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Coorg</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Nagarhole</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Ooty</span>
          <span class="circuit-dot"></span>
          <span class="circuit-stop">Mumbai</span>
        </div>"""
html = html.replace(route_old, route_new)

# 4. Update Checklist Accommodations
checklist_match = re.search(r'(<h3[^>]*>.*?Accommodations.*?</h3>.*?)(?=<h3)', html, re.DOTALL)
if checklist_match:
    checklist_old = checklist_match.group(1)
    checklist_new = """<h3>🏠 Accommodations & Stays</h3>
        <div class="check-list">
          <div class="check-item">
            <input type="checkbox" id="c5" checked>
            <label for="c5"><strong>Coorg - Beans & Blossom</strong><span>3 nights (May 20-23). Airbnb. PAID. See <code>tickets-bookings/COORG Stay.pdf</code></span></label>
          </div>
          <div class="check-item">
            <input type="checkbox" id="c6" checked>
            <label for="c6"><strong>Nagarhole - Arasu Homestay</strong><span>1 night (May 23-24). Agoda Booking #2008739872. PAID. See <code>tickets-bookings/Confirmation_for_Booking_ID_#_2008739872.pdf</code></span></label>
          </div>
          <div class="check-item">
            <input type="checkbox" id="c7" checked>
            <label for="c7"><strong>Ooty - Snowdrops Ooty</strong><span>3 nights (May 24-27). Booking.com HM5EWR9PZR. PAID. See <code>tickets-bookings/Reservation Details - HM5EWR9PZR.pdf</code></span></label>
          </div>
        </div>
        """
    html = html.replace(checklist_old, checklist_new)
else:
    print("WARNING: Checklist not found!")

# 5. Flight info
flight_old = """            <label for="c1"><strong>Flights (MUM ✈ CJB)</strong><span>Outbound May 20, Return May 27. Check luggage rules.</span></label>"""
flight_new = """            <label for="c1"><strong>Flights (MUM ✈ CJB)</strong><span>Outbound May 20, Return May 27. IndiGo PNR: 0405260074543. See <code>tickets-bookings/Flight_ETicket_0405260074543.pdf</code></span></label>"""
html = html.replace(flight_old, flight_new)

# 6. Replace Days 4, 5, 6
day_block_match = re.search(r'(<div id="day4" class="page">.*?)(?=<!-- [^\n]+DAY 7)', html, re.DOTALL)
if day_block_match:
    day_blocks_new = """<div id="day4" class="page">
    <div class="day-hero">
      <div class="day-hero-bg" style="background-image: url('images/nagarhole_tiger.jpg'); background-color:#1A1208;"></div>
      <div class="day-hero-content">
        <div class="day-badge">Day 4 · Saturday, May 23</div>
        <h2>Nagarhole Safari <span>/ The Kabini Backwaters</span></h2>
      </div>
    </div>
    <div class="day-body">
      <div class="tldr">
        <h3>TL;DR</h3>
        <p>Morning drive from Coorg to Nagarhole via Hunsur. Check in to Arasu Homestay. Afternoon/Evening jungle safari in Nagarhole National Park (Kabini). Dinner at the homestay and sleep early.</p>
        <div class="tldr-pills">
          <span class="tldr-pill pill-drive">🚗 Coorg → Nagarhole: 90 km, ~2.5 hrs</span>
          <span class="tldr-pill pill-activity">🐅 Nagarhole Evening Safari</span>
          <span class="tldr-pill pill-stay">🏡 Arasu Homestay, Nagarhole</span>
        </div>
      </div>

      <div class="logistics-card">
        <h3>Logistics & Navigation</h3>
        <div class="logistics-item"><label>Route</label><span>Coorg → Hunsur → Nagarhole</span></div>
        <div class="logistics-item"><label>Temp</label><span>28-32°C in Nagarhole</span></div>
        <div class="logistics-item"><label>Stay</label><span>Arasu Homestay (Night 4)</span></div>
      </div>

      <div class="section-divider"><span>Hour by Hour</span></div>
      <div class="timeline">
        <div class="timeline-item">
          <div class="time">09:00 AM</div>
          <div class="event">
            <h4>Check out of Beans & Blossom</h4>
            <p>Breakfast in Coorg, pack the car, and begin the drive down from the hills towards Hunsur.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">11:30 AM</div>
          <div class="event">
            <h4>Arrive at Arasu Homestay</h4>
            <p>Check in to Arasu Homestay. Rest and have an early lunch before the safari.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">03:30 PM</div>
          <div class="event">
            <span class="meal-tag tag-activity">Safari Time</span>
            <h4>Nagarhole National Park - Evening Safari</h4>
            <p>Drive to the safari gate. The evening slot (4:00 PM - 6:30 PM) is optimal for tiger and leopard sightings near the Kabini backwaters as animals come to drink.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">07:30 PM</div>
          <div class="event">
            <span class="meal-tag tag-dinner">Dinner</span>
            <h4>Dinner at Homestay</h4>
            <p>Return to Arasu Homestay for a quiet dinner and rest. Early bedtime recommended.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════ DAY 5 ═══════════════ -->
  <div id="day5" class="page">
    <div class="day-hero">
      <div class="day-hero-bg" style="background-image: url('images/36_hairpins.jpg'); background-color:#3A5C35;"></div>
      <div class="day-hero-content">
        <div class="day-badge">Day 5 · Sunday, May 24</div>
        <h2>Nagarhole → Ooty <span>/ Wildlife, Hairpins & Cloud Country</span></h2>
      </div>
    </div>
    <div class="day-body">
      <div class="tldr">
        <h3>TL;DR</h3>
        <p>The most dramatic drive of the trip. Through Mudumalai Tiger Reserve (wild elephant corridor), the legendary 36-hairpin ascent into the Nilgiris. Temperature drops 12°C through the cloud layer. Arrive Ooty by 2 PM. E-Pass checkpoint at Masinagudi — have QR code ready.</p>
        <div class="tldr-pills">
          <span class="tldr-pill pill-drive">🚗 Nagarhole → Ooty: 130 km, ~4.5 hrs</span>
          <span class="tldr-pill pill-activity">🐅 Mudumalai Wildlife Drive</span>
          <span class="tldr-pill pill-activity">⛰ 36 Hairpin Bends Ascent</span>
          <span class="tldr-pill pill-stay">🏡 Snowdrops Ooty (Night 5)</span>
        </div>
      </div>

      <div class="logistics-card">
        <h3>Logistics & Navigation</h3>
        <div class="logistics-item"><label>Route</label><span>Nagarhole → Gundlupet → Mudumalai → Masinagudi → Ooty</span></div>
        <div class="logistics-item"><label>Permit</label><span>E-Pass Required — Show QR Code at Masinagudi</span></div>
        <div class="logistics-item"><label>Speed</label><span>25 kmph strictly enforced in Mudumalai</span></div>
        <div class="logistics-item"><label>Stay</label><span>Snowdrops Ooty (Night 5)</span></div>
      </div>

      <div class="section-divider"><span>Hour by Hour</span></div>
      <div class="timeline">
        <div class="timeline-item">
          <div class="time">08:00 AM</div>
          <div class="event">
            <h4>Check out of Arasu Homestay</h4>
            <p>Breakfast and depart for Ooty. The route cuts through Bandipur and Mudumalai.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">10:00 AM</div>
          <div class="event">
            <h4>Mudumalai Forest Drive</h4>
            <p>Enter the tiger reserve. Strict speed limit, do not stop or step out of the vehicle. High probability of spotting elephants.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">11:30 AM</div>
          <div class="event">
            <h4>Masinagudi Checkpost & Ascent</h4>
            <p>Show the Nilgiris E-Pass here. Begin the 36-hairpin climb. Use lower gears continuously; avoid riding the brakes.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">02:00 PM</div>
          <div class="event">
            <h4>Arrive in Ooty & Check in to Snowdrops</h4>
            <p>Check in to Snowdrops Ooty. The temperature will be notably cooler. Rest and acclimate.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">04:30 PM</div>
          <div class="event">
            <h4>Doddabetta Peak or Ooty Lake</h4>
            <p>Optional evening visit to Doddabetta Peak (highest in Nilgiris) or a relaxing boat ride on Ooty Lake.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════ DAY 6 ═══════════════ -->
  <div id="day6" class="page">
    <div class="day-hero">
      <div class="day-hero-bg" style="background-image: url('images/ooty_landscape.jpg'); background-color:#1A2E14;"></div>
      <div class="day-hero-content">
        <div class="day-badge">Day 6 · Monday, May 25</div>
        <h2>Ooty — Rose Garden & Botanical Gardens <span>/ Ooty Full Day 1</span></h2>
      </div>
    </div>
    <div class="day-body">
      <div class="tldr">
        <h3>TL;DR</h3>
        <p>Full day in Ooty. Morning at the 160-year-old Government Botanical Gardens (650 plant species). Ooty Rose Garden with 20,000 rose varieties in bloom. Afternoon tea estate visit. Sunset overlooking the Nilgiri valleys. Dinner at a local cafe.</p>
        <div class="tldr-pills">
          <span class="tldr-pill pill-activity">🌺 Rose Garden (20,000 Varieties)</span>
          <span class="tldr-pill pill-activity">🌿 Botanical Gardens (1847)</span>
          <span class="tldr-pill pill-food">🍵 Tea Tasting & Tour</span>
          <span class="tldr-pill pill-stay">🏡 Snowdrops Ooty (Night 6)</span>
        </div>
      </div>

      <div class="logistics-card">
        <h3>Logistics & Navigation</h3>
        <div class="logistics-item"><label>Total Drive</label><span>Local day in Ooty</span></div>
        <div class="logistics-item"><label>Stay</label><span>Snowdrops Ooty (Night 6)</span></div>
        <div class="logistics-item"><label>Weather</label><span>14–22°C — Carry a Light Fleece All Day</span></div>
      </div>

      <div class="section-divider"><span>Hour by Hour</span></div>
      <div class="timeline">
        <div class="timeline-item">
          <div class="time">09:00 AM</div>
          <div class="event">
            <h4>Botanical Gardens</h4>
            <p>Arrive early to beat the crowds. Explore the sprawling 55-acre gardens established in 1847.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">11:30 AM</div>
          <div class="event">
            <h4>Rose Garden</h4>
            <p>Visit the Government Rose Garden, home to one of the largest collections of roses in India.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">01:30 PM</div>
          <div class="event">
            <span class="meal-tag tag-lunch">Lunch</span>
            <h4>Lunch at Sidewalk Cafe or Earl's Secret</h4>
            <p>Enjoy a cozy lunch in town.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">03:00 PM</div>
          <div class="event">
            <h4>Tea Museum / Factory Visit</h4>
            <p>Learn about Nilgiri tea processing and enjoy a fresh tasting session.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="time">06:00 PM</div>
          <div class="event">
            <h4>Return to Snowdrops Ooty</h4>
            <p>Relax at the hotel for the evening.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
"""
    html = html[:day_block_match.start()] + day_blocks_new + '\n  ' + html[day_block_match.end():]
else:
    print("WARNING: Day 4-6 block not found!")

# 7. Replace any remaining 'Savoy Hotel' references in Day 7/8
html = html.replace('Savoy Hotel, Ooty (Night 7)', 'Snowdrops Ooty (Night 7)')
html = html.replace('Savoy Hotel, 8:00 AM', 'Snowdrops Ooty, 11:00 AM')
html = html.replace('Savoy Hotel', 'Snowdrops Ooty')
html = html.replace('Savoy hotel', 'Snowdrops Ooty')
html = html.replace('Savoy', 'Snowdrops')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Rebuilt Nagarhole itinerary cleanly!")
