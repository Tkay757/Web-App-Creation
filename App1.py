import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(page_icon=":<N:" , page_title = "Apple INC.", layout = "wide")

def lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

img = Image.open("head.jpeg")
imgfont= Image.open("font.jpeg")

with st.container():
     x,y,z = st.columns([2.8,2,2.7])
     with y:
      st.image(imgfont)
          
with st.container():
        a,b,c = st.columns([0.5,3,0.5])
with b:
    st.image(img)
    st.subheader("Starting from ¹ 1,49,000")
    st.button("Book Now")
with st.container():
     st.write("___")
     st.video("apple.mp4")
     col1, col2, col3, col4 = st.columns(4)
     
     #Images
     img1 =Image.open("back.jpeg")
     img2 =Image.open("front.jpeg")
     img3 =Image.open("colours.jpeg")
     img4 =Image.open("a17.jpeg")
     img6 =Image.open("glow.jpeg")
     img7 =Image.open("camera2.jpeg")
     img8 =Image.open("face.jpeg")
     img9 =Image.open("specs.jpeg")
     img10=Image.open("cateye.jpeg")
     img11=Image.open("game 1.jpeg")
     img12=Image.open("game title.jpeg")
     img13=Image.open("mac.jpeg")
     img14=Image.open("f.jpeg")
     img15=Image.open("pods.jpeg")
     img16=Image.open("wa.jpeg")
     img17=Image.open("Mac logo.jpeg")
     img18=Image.open("iphone logo.jpeg")
     img19=Image.open("watch logo.jpeg")
     img20=Image.open("air title.jpeg")
    #1st Set 4 columns
    #Col1
     with col1:
        st.image(img1)
        st.write("""Pro camera system
48MP Main: 24 mm, ’/1.78 aperture, 
secondgeneration sensorshift optical image stabilisation, 
100% Focus Pixels, 
support for superhighresolution photos (24MP and 48MP)
12MP Ultra Wide: 13 mm,
’/2.2 aperture and 120° field of view,
100% Focus Pixels
12MP 2x Telephoto (enabled by quadpixel sensor): 48 mm,
’/1.78 aperture, secondgeneration sensorshift optical image stabilisation, 100% Focus Pixels
12MP 3x Telephoto: 77 mm, 
’/2.8 aperture, 
optical image stabilisation
3x optical zoom in,
2x optical zoom out;
6x optical zoom range
Digital zoom up to 15x""")     
     
     #Col2
     with col2:
         st.image(img2)
         st.write("""CUPERTINO, CALIFORNIA Apple's
                   Powerful camera upgrades enable the equivalent of seven pro lenses with incredible image quality,
                   including a more advanced 48MP Main camera system that now supports the new super-high-resolution 24MP default,
                   the next generation of portraits with Focus and Depth Control, improvements to Night mode and Smart HDR, 
                   and an all-new 5x Telephoto camera exclusively on iPhone 15 Pro Max. 
                   A17 Pro unlocks next-level gaming experiences and pro performance.""")
     #Col3
     with col3:
         st.image(img3)
         st.write("""In addition to the new titanium alloy frame, 
                  the iPhone 15 Pro features the thinnest borders ever on an iPhone, 
                  allowing Apple to reduce the overall dimensions of the phone itself without sacrificing display size. 
                  The iPhone 15 Pro features a 6.1-inch display, 
                  and the iPhone 15 Pro Max features a 6.7-inch display -- the same display size as the iPhone 14 Pro and 14 Pro Max.
                  The titanium finish features a brushed texture and comes in four colors, including black, white, blue and natural titanium.
                  Apple is also making the iPhone 15 Pro easier to repair, 
                  thanks to a new, recycled aluminum substructure that allows for the back glass to be easily replaced.""")
     
     #Col4 
     with col4:
         st.image(img4)
         st.write("""A17 Pro chip gets performance boost by up to 10 per cent compared to the predecessors. 
                  The new system-on-chip has a 6-core CPU, which includes two high performance cores and four efficiency cores.
                  For the GPU (Graphics Processing Unit), 
                  Apple said it has completely redesigned to feature a 6-core GPU on the A17 Pro chip. 
                  Apple said the new GPU design will boost the performance by up to 20 per cent while being more power efficient. 
                  The GPU on the A17 Pro supports hardware-accelerated Ray Tracing, 
                  which is said to enhance the graphics while gaming on the iPhone 15 Pro series smartphones. 
                  Ray Tracing technique realistically simulates the lightning in a scene to produce life-like reflections and shadows.""")

st.write("_____")

with st.container():
   st.title("5ö5ã5õ5ü5û5ò 5í5ñ BUT zOOmed")

   l,m,n = st.columns([1.5,3,1.5])
with m:
   st.image(img6)


   st.image(img7)



st.write("_____")

with st.container():
     st.write("___")
     c1, c2, c3, c4 = st.columns([1.5,1,1,1.5])


     with c1:
         st.subheader("""FORGED IN TITANIUM 
iPhone 15 Pro Max has a strong and light aerospace-grade titanium design with a textured matt-glass back. 
It also features a Ceramic Shield front thats tougher than any smartphone glass. And its splash, water and dust resistant.
ADVANCED DISPLAY  The 17.00 cm (6.73) Super Retina XDR display with ProMotion ramps up refresh rates to 120Hz when you need exceptional graphics performance. 
Dynamic Island bubbles up alerts and Live Notifications. Plus, with Always-On display, 
your Lock Screen stays glanceable, so you dont have to tap it to stay in the know.""")
     
     with c4:
         st.subheader("""GAME CHANGING A17 PRO CHIP  
A Pro-class GPU makes mobile games feel so immersive, with rich environments and realistic characters. A17 Pro is also incredibly efficient and helps to deliver amazing all-day battery life.
POWERFUL PRO CAMERA SYSTEM  Get incredible framing flexibility with 7 pro lenses. Capture super-high-resolution photos with more colour and detail using the 48MP Main camera. And take sharper close-ups from farther away with the 5x Telephoto camera on iPhone 15 Pro Max.
CUSTOMISABLE ACTION BUTTON  Action button is a fast track to your favourite feature.""")

with st.container():
     o1, o2, o3 = st.columns([0.9,3,1])

     with o2:
         st.image(img8)


with st.container():
     b1, b2, b3, b4 = st.columns([1.5,1,1,1.5])

with b1:
    st.subheader("""PRO CONNECTIVITY 
The new USB-C connector lets you charge your Mac or iPad with the same cable you use to charge iPhone 15 Pro Max. With USB 3, 
you get a huge leap in data transfer speeds. And you can download files up to 2x faster using Wi-Fi 6E.
VITAL SAFETY FEATURES  With Crash Detection, iPhone can detect a severe car crash and call for help if you cant.""")
    
with b4:
    st.subheader("""DESIGNED TO MAKE A DIFFERENCE  
iPhone comes with privacy protections that help keep you in control of your data. 
Its made from more recycled materials to minimise environmental impact. 
And it has built-in features that make iPhone more accessible to all.
COMES WITH APPLECARE WARRANTY  Every iPhone comes with a one-year limited warranty and up to 90 days of complimentary technical support.""")
    
with st.container():
    aa,ab,ac = st.columns([0.5,3,0.5])

with ab:
  st.image(img9)
st.header("The More You Focus")
st.subheader("The More It Gets Clear")
with st.container():
    a1,a2,a3 = st.columns([0.1,3,0.1])
    with a2:
      st.image(img10)
st.image(img12)
with st.container():
    xx,xy,xz = st.columns([0.5,3,0.5])
with xy:    
  st.image(img11)

with st.container():
    zoom1,zoom2 = st.columns([5,2.5])

    zoomI = Image.open("edited2.jpeg")
with zoom1:
    st.image(zoomI)
with zoom2:
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.header("Oops iPhone is DROWNING")
    st.subheader("No WORRIES!!!")
    st.subheader("WATERPROOF RESISTANCE")
    st.write("""Apple states all the 15s can tolerate submersion in water to 18 meters for up to 30 minutes. 
                While that technically is not waterproof (due to time limit) it certainly qualifies as highly water resistant.
                While I certainly wouldnt use it as dive camera, I also wouldnt worry about fumbling it in a swimming pool as long as you retrieve it promptly.
                Apple does state that scratches and dents can obviously impact its water resistance. """)
    
st.title("For You!!!")
st.subheader("Based on your Intrests")
with st.container():
    ll,lm,ln,lo = st.columns(4)

with ll:
    st.image(img17)
    st.image(img13)
    st.header("FROM ¹1,10,000")
    st.markdown("[:desktop_computer:](https://www.apple.com/in/shop/buy-mac?afid=p238%7CsTNTAZuTm-dc_mtid_187079nc38483_pcrid_694334137146_pgrid_109263622693_pntwk_g_pchan__pexid__ptid_kwd-993637709_&cid=aos-IN-kwgo-mac--slid---product-)") 

with lm:
    st.image(img18)
    st.image(img14)
    st.header("FROM ¹75,000")
    st.markdown("[=ñ](https://www.apple.com/in/iphone/?afid=p238%7CsnTdg5ZpO-dc_mtid_209254ho67063_pcrid_691391430198_pgrid_135363319397_pexid__&cid=wwa-in-kwgo-iphone-slid----Evergreen-)")
    
with ln:
    st.image(img19)
    st.image(img16)
    st.header("FROM ¹30,000")
    st.markdown("[](https://www.apple.com/in/watch/?afid=p238%7Cs4R9CQuTi-dc_mtid_187079nc38483_pcrid_694334137104_pgrid_115404494361_pntwk_g_pchan__pexid__ptid_kwd-52218226_&cid=aos-IN-kwgo-watch--slid---product-)")

with lo:
    st.image(img20)
    st.image(img15)
    st.header("FROM ¹15,000")
    st.markdown("[<§](https://www.apple.com/in/airpods/)")

st.write("___")

with st.container():

    st.write("""*Listed pricing is Maximum Retail Price (inclusive of all taxes).
1.No Cost EMI is available with the purchase of an eligible product made using qualifying cards on 3- or 6-month tenures from most leading banks. 
  Until 26 June 2024, No Cost EMI is available with the purchase of an eligible iPhone made using qualifying cards on 3-, 6-, 9-, 12-, 18- or 24-month tenures from most leadings banks. 
  Monthly pricing is rounded to the nearest rupee. Exact pricing will be provided by your bank, subject to your banks terms and conditions. Minimum order spend applies as per your card-issuing bank threshold. 
  Offer cannot be combined with Apple Store for Education or Corporate Employee Purchase Plan pricing. Card eligibility is subject to terms and conditions between you and your card-issuing bank. Offer may be revised or withdrawn at any time without any prior notice. Terms apply.
            
2.Representative example:
Based off a 6-month tenure. ¹79900.00 total cost includes 15% p.a. and No Cost EMI savings of ¹3380.00, paid over 6 months as six monthly payments of ¹13317.00.
Based off a 24-month tenure. ¹79900.00 total cost includes 15% p.a. and No Cost EMI savings of ¹11242.00, paid over 24 months as 24 monthly payments of ¹3329.00.
            
3.Display size: The display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 15.54 cm / 6.123 (iPhone 15 Pro) or 17.00 cm / 6.693 (iPhone 15 Pro Max) diagonally. Actual viewable area is less.
            
4.iPhone 15 Pro and iPhone 15 Pro Max are splash, water and dust resistant, and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529 (maximum depth of 6 metres up to 30 minutes). 
  Splash, water and dust resistance are not permanent conditions. Resistance might decrease as a result of normal wear. Do not attempt to charge a wet iPhone; refer to the user guide for cleaning and drying instructions. Liquid damage is not covered under warranty.
            
5.Stand is sold separately.
            
6.USB 3 cable with 10 Gbps speed is required.
            
7.WiFi 6E available in countries and regions where supported.
            
8.The included USBC Charge Cable is compatible with AirPods Pro (2nd generation) with MagSafe Charging Case (USBC).
            
9.Testing conducted by Apple in August 2023 using preproduction iPhone 15, iPhone 15 Plus, iPhone 15 Pro and iPhone 15 Pro Max units and software and accessory Apple USB-C Power Adapter (20W Model A2305). Fast-charge testing conducted with drained iPhone units. Charge time varies with settings and environmental factors; actual results will vary.
            
10.Ultra Wideband availability varies by region.
            
11.Use of eSIM requires a wireless service plan (which may include restrictions on switching service providers and roaming, even after contract expiration). Not all carriers support eSIM. Use of eSIM in iPhone may be disabled when purchased from some carriers. See your carrier for details. To learn more, visit apple.com/in/esim.
            
12.Data plan is required. 5G is available in selected markets and through selected carriers. Speeds vary based on site conditions and carrier. For details on 5G support, contact your carrier and see apple.com/in/iphone/cellular.
            
13.All battery claims depend on network configuration and many other factors; actual results will vary. Battery has limited recharge cycles and may eventually need to be replaced. Battery life and charge cycles vary by use and settings. See apple.com/in/batteries and apple.com/in/iphone/battery.html for more information.
            
14.Accessories are sold separately.
            
15.iPhone 15 and iPhone 15 Pro can detect a severe car crash and call for help. Requires a cellular connection or WiFi calling.
            
16.On a mass balance allocation.
            
17.Breakdown of U.S. retail packaging by weight. Adhesives, inks and coatings are excluded from our calculations of plastic content and packaging weight.
            
18.Responsible sourcing of wood fibre is defined in Apples Responsible Fibre Specification. We consider wood fibres to include bamboo.
            
19.Door Detection and Point and Speak can read signs and labels in Cantonese (Simplified, Traditional), Chinese (Simplified, Traditional), English (U.S.), French (France), German (Germany), Italian (Italy), Japanese (Japan), Korean (Korea), Portuguese (Brazil), Russian (Russia), Spanish (Spain) and Ukrainian (Ukraine). Detection Mode should not be relied on in circumstances where you may be harmed or injured or in high-risk or emergency situations.
            
20.Requires an iPhone and Apple Watch with second-generation Ultra Wideband chip. Ultra Wideband availability varies by region.
            
21.Trade-in values will vary based on the condition, year and configuration of your trade-in device, and is computed on Maximum Retail Price. You must be at least 18 years old to be eligible to trade in for credit. Not all devices are eligible for credit. More details are available from Apples trade-in partner for trade-in and recycling of eligible devices. Restrictions and limitations may apply. Credit applied towards your new iPhone will be based on the received device matching the description you provided when your estimate was made and upon validation by the courier. Apple reserves the right to refuse or limit the quantity of any device for any reason.
            
22.Battery life claim refers to larger models. All battery claims depend on network configuration and many other factors; actual results will vary. Battery has limited recharge cycles and may eventually need to be replaced. Battery life and charge cycles vary by use and settings. See apple.com/in/batteries and apple.com/in/iphone/battery.html for more information.
            
23.Apps are available on the App Store. Title availability is subject to change.
            
24.Apple TV+ requires a subscription.""")

st.write("___")
st.container()
cc,bb,aa = st.columns(3)

with bb:
    st.image("Logowithword.jpeg")
st.container()

s1,s2,s3,s4 = st.columns(4)

with s1:
    st.header("About Apple")
    st.write("""Apple Inc. is an American multinational corporation and technology company headquartered in Cupertino, California, in Silicon Valley. 
             It designs, develops, and sells consumer electronics, computer software, and online services. 
             Devices include the 
             iPhone, 
             iPad, 
             Mac, 
             Apple Watch, 
             Vision Pro,
             Apple TV 
             and operating systems include 
             iOS, 
             iPadOS, 
             macOS 
             and software applications and services include 
             iTunes, 
             iCloud, 
             Apple Music
             Apple TV+.""")
    
with s2:
    st.header("Store Lists")
    st.write("International Branches (Apple Inc.)")
    st.write("""United States--Japan--
            United Kingdo--Canada--
            Italy--Austraila--China--
            Switzerland--Germany--
            France--Spain--Hong Kong--
            Netherlands--Sweden--Brazil--
            Turkey--Belgium--
            United Arab Emirates (UAE)--
            Macau--Mexico--Singapore--Taiwan--
            South Korea--Austria--Thailand--
            India--Malaysia""")
    
with s3:
    st.header("Check out")
    st.image("website.jpeg")
    st.write("iPad") 
    st.markdown("[Apple iPad](https://www.apple.com/in/ipad/?afid=p238%7Cswf56Q2l8-dc_mtid_187079nc38483_pcrid_702200531022_pgrid_114045531335_pntwk_g_pchan__pexid__ptid_kwd-662952649_&cid=aos-IN-kwgo-ipad--slid---product-)")
    st.write("WWDC")
    st.markdown("[Apple WWDC](https://developer.apple.com/wwdc24/)")

with s4:
    st.header("CONTACT")
    st.subheader("Apple Inc One Apple Park Way; Cupertino, CA 95014, U.S.A.")

