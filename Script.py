class script(object):
    START_TXT = """πα΄ΚΚα΄ {},

 π Κ π‘α΄α΄α΄ Ιͺπ  α΄α΄α΄α΄ κ°ΙͺΚα΄α΄Κ

π¨'π πΊ π΄ππΎπ-π₯πππΎππ½ππ πππππ π¬πΊππΊππΎπ 
β’ <b>Build Version</b>: <code>V2.1.0 [BETA]</code>
β’ <b>Speciality</b>: <code>Movie Provider</code>
π’πππΌπ <b>π§πΎππ</b> ππ ππ π₯πππΌπππππ<a href='https://telegra.ph/file/eaf97e4782f05b667e551.jpg'>.</a>"""
    
    HELP_TXT = """<b>π§πΎππΎ ππ πππΎ π΄πππΊπ πΌππππΊππ½π:</b>
"""
    GTRANS_TXT = """<b>π³ππΊππππΊπππ</b>
- π³ππΊππππΊππΎ ππΎπππ ππ πΊ πππΎπΌππΏππΌ ππΊππππΊππΎ!
<b>π’ππππΊππ½π πΊππ½ π΄ππΊππΎ:</b>
- /tr [language code][reply] - π³ππΊππππΊππΎ ππΎππππΎπ½ ππΎπππΊππΎ ππ πππΎπΌππΏππΌ ππΊππππΊππΎ.
"""
    PASTE_TXT = """<b>π―πΊπππΎ</b>
- π―πΊπππΎ ππππΎ ππΎπππ ππ π½ππΌπππΎπππ ππ πΊ ππΎπ»ππππΎ!
<b>π’ππππΊππ½π πΊππ½ π΄ππΊππΎ:</b>
- /paste [text] - π―πΊπππΎ πππΎ ππππΎπ ππΎππ ππ ππΊπππ
- /paste [reply] - π―πΊπππΎ πππΎ ππΎππππΎπ½ ππΎππ ππ ππΊπππ
"""
    STICK_TXT = """<b>π²πππΌππΎπ π¨π£</b>
- π³πππ πΌππππΊππ½ ππ πππΎπ½ ππ ππΎπ πΊ π¨π£ ππΏ πΊπ ππππΌππΎπ

<b>Command</b>
- /stickerid - π¦πΎπ π¨π£
"""
    ABOUT_TXT = """
ππ² πππ¦π :α΄Κα΄Ι΄α΄Ιͺ ΙͺΙ’α΄Κα΄ π

π¦ ππ«πππ­π¨π« :ΚΚα΄ssα΄Ι΄[TG]π·

ππππ§π π?ππ π : ππ²π­π‘π¨π§

πππ’ππ«ππ«π² : ππ²π«π¨π π«ππ¦ ππ¬π²π§ππ’π¨ 

πππ?π©π©π¨π«π­ππ ππ’π­π : ππ§π₯π² πππ₯ππ π«ππ¦

ππππ«π―ππ« : πππ«π¨π€U

ππππ­ππππ¬π : ππ¨π§π π¨ππ

πππ?π’π₯π sπ­ππ­π?π¬ : π2.1 [ππππ]
"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a closed source project.   

CODES:
1. Auto Filter
2. Group Managing  
"""
    TTS_TXT = """<b>TEXT TO SPEACH</b>
Simple Telegram Text-To-Speech Module.
It can use the following as speech synthesis engines:

Amazon's Polly engine
Google's TTS engine by way of the gTTS library
"""
    COVID_TXT = """<b><u>π’ππππ½ 19 πππΏππππΊππππ</u><b/>
π’πππππΊ πππΏππππΊππππ ππΏ ππππ πΌππππππ / π³π ππππ πππΎ πΌππππ½ πππΏπ ππΏ πΊππ πΌππππππ            
<b>π’ππππΊππ½:</b>
/covid [country name] - π¦πΎπ πππΏπ πΊπ»πππ πΌππππ½ πΌπΊππΎπ ππ ππππ πΌππππππ
<b>π΄ππΊππΎ</b>
- π’ππππ½ π»πΎ πππΎπ½ ππ ππ πΊππ½ ππππππ
    """
    BAN_TXT = """<b>π‘πΊππ:</b>
π²πππΎ ππΎππππΎ ππΎπΎπ½ ππ π»πΎ πππ»πππΌππ π»πΊπππΎπ½; πππΊπππΎππ, πΊπππππΊππΌπΎπ, ππ ππππ ππππππ.  
π³πππ πππ½πππΎ πΊπππππ πππ ππ π½π πππΊπ πΎπΊππππ, π»π πΎπππππππ ππππΎ πΌπππππ πΊπΌπππππ, ππ πΎππΎπππππΎ ππππ ππΎπΎ!

<b>π π½πππ π’ππππΊππ½π:</b>
- /ban - π‘πΊπ πΊ πππΎπ
- /tban - π³πΎπππππΊππππ π»πΊπ πΊ πππΎπ. π€ππΊππππΎ ππππΎ ππΊπππΎπ: π¦π = π¦ ππππππΎπ, π₯π = π₯ πππππ, π¨π½ = π¨ π½πΊππ, π§π = π§ ππΎπΎππ.
- /unban - π΄ππ»πΊπ πΊ πππΎπ

<b>π€ππΊππππΎπ:</b>
- π‘πΊπ πΊ πππΎπ πΏππ πππ πππππ. 
-> /tban @πππΎπππΊππΎ π€π
"""
    PING_TXT= """<b>π―πππ:</b>

π§πΎπππ πππ ππ ππππ ππππ ππππ, π¨π πππππ-ππΎπππ 'ππ'.

<b>π’ππππΊππ½π:</b>

- /alive - π³π πΌππΎπΌπ πππΎπππΎπ πππ πΊππΎ πΊππππΎ
- /hi - π­π ππ, π‘ππ ππΊππΎπ ππ
- /ping - π³π πͺπππ ππππ ππππ 

<b>π΄ππΊππΎ:</b>

β’ π³πππ πΌππππΊππ½ πΌπΊπ π»πΎ πππΎπ½ ππ πππ πΊππ½ ππππππ.
β’ π³πππ πΌππππΊππ½ πΌπΊπ π»πΎ πππΎπ½ π»ππ πΎππΎπππππΎ ππ ππππππ πΊππ½ π»πππ ππ.
"""
    JSON_TXT = """<b>π©πππ:</b>
π‘ππ ππΎπππππ ππππ πΏππ πΊππ ππΎππππΎπ½ ππΎπππΊππΎπ ππππ /json. 
<b>π₯πΎπΊππππΎπ:</b>
π¬πΎπππΊππΎ π€π½ππππππ JSON
π―π π²ππππππ 
π¦ππππ π²ππππππ
"""
    FUN_TXT ="""<b>π₯ππ π¬ππ½πππΎπ</b> 
    
<b>π² π­ππππππ πππΌπ ππππ ππππΎ πΏππ ππππΏπΏπ</b>
πππ πππΎππΎ πππ: 
π£. /dice - π±πππ πππΎ π½ππΌπΎ
π€. /Throw ππ /Dart - π³π πππππ πΊ π½πΊππ
3. /Runs - π©πππ ππππΎ ππΊππ½ππ π½πΊππππππΎπ
4. /Goal or /Shoot - π³π πππΊπ ππ πππππ πΊ π»πΊππ
"""
    PURGE_TXT ="""<b>π―ππππΎ</b>
- π£πΎππΎππΎ πΊ ππππ ππΏ ππΎπππΊππΎπ πΏπππ πΊ πππππ!
    
 <b>π π½πππ</b> 
β /purge :- π£πΎππΎππΎ πΊππ ππΎπππΊππΎπ πΏπππ πππΎ ππΎππππΎπ½ ππΎπππΊππΎ ππ, π³ππΎ πΌππππΎππ ππΎπππΊππΎ
    """
    MANUELFILTER_TXT = """<b>π₯ππππΎππ</b>
π₯ππππΎπ ππ πππΎ πΏπΎπΊππππΎ ππΎππΎ πππΎππ πΌπΊπ ππΎπ πΊπππππΊππΎπ½ ππΎππππΎπ πΏππ πΊ ππΊππππΌπππΊπ ππΎπππππ½ πΊππ½ πππΎ π»ππ ππππ ππΎπππππ½ πππΎππΎππΎπ πΊ ππΎπππππ½ ππ πΏππππ½ πππΎ ππΎπππΊππΎ 
<b>π­π?π³π€:</b>
π£. π»ππ ππππππ½ ππΊππΎ πΊπ½πππ ππππππππΊππΎ ππ πππ½πΎπ ππ ππΎπππ πΏππππΎππ ππ πΊ πΌππΊπ. 
π€. ππππ πΊπ½ππππ πΌπΊπ πΊπ½π½ πΏππππΎππ ππ πΊ πΌππΊπ. 
π₯. πΏππππΎππ π½ππΎπ πππππππ πΊππ πππΎ ππΎππΎπππΊπ ππΊπππ½ππππ, ππΎπ½ππΊπ πΊππ½ π»ππππππ. 
π¦. πΊππΎππ π»ππππππ πΊππΎ πΊπππ ππππππππΎπ½ ππππ πΊ πππππ ππΏ π¨π¦ πΌππΊππΊπΌππΎππ. 
π§. πππΎππΎ πΊππΎ ππππΎ πΎπΊπππΎπ πΎπππ, πππ ππ πΏπππ½ ππ πππ. 
<b>π’ππππΊππ½π πΊππ½ π΄ππΊππΎ:</b>
/filter  ππ /add - πΊπ½π½ πΊ πΏππππΎπ
/filters ππ /viewfilters - ππππ πΊππ πππΎ πΏππππΎππ ππΏ πΊ πΌππΊπ 
/stop ππ /del - π½πΎππΎππΎ πΊ πππΎπΌππΏππΌ πΏππππΎπ (ππΎππΊππΊππΎ ππΎπππππ½π ππππ πππΊπΌπΎπ πΏππ π½πΎππΎππππ ππππππππΎ πΏππππΎππ πΊπ πΊ ππππΎ) 
/stopall ππ /delall - π½πΎππΎππΎ πππΎ πππππΎ πΏππππΎππ ππ πΊ πΌππΊπ (πΌππΊπ ππππΎπ ππππ)
"""
    SONG_TXT = """<b>π²πππ π£ππππππΊπ½ π¬ππ½πππΎ</b>
- π¨πΏ πππ ππΊππ ππ π½ππππππΊπ½ πΊ ππππ, π½ππ'π ππΎπΊππΌπ πΏππ ππππΎπ π»ππ ππΎππΎ ππ πππΎ πΊππ ππ πππΎ π»ππ
<b>π’ππππΊππ½</b>
- /song [Song Name] - π³π ππΎπ πππΎ ππππ
<b>Usage</b>
- π’πΊπ π»πΎ πππΎπ½ π»π πΎππΎππ πππΎ
- πΆππππ ππππ ππ π»πππ ππ
<b>π‘ππ</b>
π²πππΎππππΎπ ππ ππππ ππππ πΊπ πΎππππ!
"""
    MUTE_TXT = """<b>π¬πππΎ:</b>

π²πππΎ ππΎππππΎ ππΎπΎπ½ ππ π»πΎ πππ»πππΌππ Muted; πππΊπππΎππ, πΊπππππΊππΌπΎπ, ππ ππππ ππππππ.  
π³πππ πππ½πππΎ πΊπππππ πππ ππ π½π πππΊπ πΎπΊππππ, π»π πΎπππππππ ππππΎ πΌπππππ πΊπΌπππππ, ππ πΎππΎπππππΎ ππππ ππΎπΎ!   

<b>π π π½πππ πΌππππΊππ½π:</b>

- /mute - π¬πππΎ π  π΄ππΎπ 
- /tmute - π³πΎπππππΊππππ π¬πππΎ πΊ πππΎπ. π€ππΊππππΎ ππππΎ ππΊπππΎπ: π¦π = π¦ ππππππΎπ, π₯π = π₯ πππππ, π¨π½ = π¨ π½πΊππ, π§π = π§ ππΎπΎππ. 
- /unmute - π΄πmute πΊ πππΎπ.  
π€ππΊππππΎπ:
- π¬πππΎ πΊ πππΎπ πΏππ πππ πππππ. 
-> /tmute @πππΎπππΊππΎ π€π
"""
    CNTRY_TXT = """Use /Country (Country name)
- Get info about Country 
"""
    TRNT_TXT = """This feature will be added soon"""
    SHORT_TXT = """To Short your big urls
- Command /Short Link 
"""
    WEATHER_TXT = """Under development"""
    BUTTON_TXT = """Help: <b>π‘ππππππ</b>
@The_obanai_bot ππππππππ π»πππ πππ πΊππ½ πΊππΎππ ππππππΎ π»ππππππ, πππ ππΎππ ππΎπΎ πππ ππ πππππΎππΎππ ππ. 
<b>π­π‘:</b>
π£. π³πΎππΎπππΊπ ππππ πππ πΊπππππ πππ ππ ππΎππ½ π»ππππππ πππππππ πΊππ πΌππππΎππ, ππ πΌππππΎππ ππ ππΊππ½πΊππππ. 
π€. π³πππ π»ππ ππππππππ π»ππππππ ππππ πΊππ ππΎππΎπππΊπ ππΎπ½ππΊ ππππΎ. 
π₯. π‘ππππππ ππππππ½ π»πΎ πππππΎπππ πΏππππΊπππΎπ½ πΊπ π»πΎπππ ππ πΎπππΎ ππΎππππ ππππ π»πΎ ππΊππΏππππΎπ½. 
<b>π΄π±π« π»ππππππ:</b>
- ππππππΎ π»πππππ 
<code>[π‘πππππ](π»ππππππππ://π.ππΎ/ππΊππππΊπ»πππππ½πΊππΎπ)</code>
- π£πππ»ππΎ π»πππππ 
<code>[π‘ππππππ£](π»ππππππππ://π.ππΎ/telegram)
[π‘ππππππ€](π»ππππππππ://π.ππΎ/telegram)</code>
- π£πππ»ππΎ π»ππππππ ππ π²πΊππΎ π±πΊπ 
<code>[π‘ππππππ£](π»ππππππππ://π.ππΎ/ππΊππππΊπ»πππππ½πΊππΎπ)
[π‘ππππππ€](π»ππππππππ://π.ππΎ/ππΊπππππππΎππ:ππΊππΎ)</code>
<b>π ππΎππ π»ππππππ:</b>
<code>[π‘πππππ](π»ππππππΊππΎππ:ππππ ππ πΊπ πΊππΎππ!)</code>
"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>
<b>π­πππΎ:</b>
π£. π¬πΊππΎ ππΎ πππΎ πΊπ½πππ ππΏ ππππ πΌππΊπππΎπ ππΏ ππ'π πππππΊππΎ. 
π€. ππΊππΎ ππππΎ πππΊπ ππππ πΌππΊπππΎπ π½ππΎπ πππ πΌππππΊπππ πΌπΊπ πππ, ππππ πΊππ½ πΏπΊππΎ πΏπππΎπ. 
π₯. π₯ππππΊππ½ πππΎ ππΊππ ππΎπππΊππΎ ππ ππΎ ππππ πππππΎπ.  π¨'ππ πΊπ½π½ πΊππ πππΎ πΏπππΎπ ππ πππΊπ πΌππΊπππΎπ ππ ππ π½π».
"""
    CONNECTION_TXT = """<b>π’ππππΎπΌπππππ</b>
π΄ππΎπ½ ππ πΌππππΎπΌπ π»ππ ππ π―π¬ ππππΌπ ππΎπ ππππ πππ ππ πΎππΎπΌπππΎ π»πππ πππππΊπ πΏππππΎπ ππΎππΊππΎπ½ πΌππππΊππ½π πΊππ½ ππππΎ ππππΎπ ππΎπππππππΎ πΌππππΊππ½π πππππ πΏπππ πππΎ π―π¬ πππΊπ ππππ ππΎπΏππΎπΌπ ππ πππΎ πππππ ππππΌπ ππΎπππ πππ ππ ππΎπΎπ πππΎ πΏππππΎπ πΊπ½π½ππππππ πΊππ½ ππππΎπ ππππΏπΏπ πππππΊππΎ πΊππ½ ππΎπππ ππ πππΎππΎππ πΏππππ½πππ. 
π­π?π³π€:
π£. π?πππ πΊπ½ππππ πΌπΊπ πΊπ½π½ πΊ πΌππππΎπΌππππ. 
π€. π¨π πΊ πΌππΊπ πππ πΌπΊπ ππππππ πππΎ πππΎ /connect πΏππ πππΊπππππ πΊ πΌππππΎπΌππππ  
π₯. π¨π π―π¬ πππ ππππ πππΎπΌππΏπ πΌππΊπ ππ½ πππππ πΊπΏππΎπ πππΎ πΌππππΊππ½. 
π’ππππΊππ½π πΊππ½ π΄ππΊππΎ: 
/connect - πΌππππΎπΌπ πΊ ππΊππππΌπππΊπ πΌππΊπ ππ ππππ π―π¬ 
/disconnect  - π½πππΌππππΎπΌπ πΏπππ πΊ πΌππΊπ 
/connections - ππππ πΊππ ππππ πΌππππΎπΌπππππ

"""
    FILTER_TXT ="""π²πΎππΎπΌπ πΊ πΏππππΎπ ππππΎ π»πΎπππ:"""
    PIN_TXT = """<b>π―π¨π­:</b>
π ππ πππΎ πππ ππΎππΊππΎπ½ πΌππππΊππ½π πΌπΊπ π»πΎ πΏππππ½ ππΎππΎ; ππΎπΎπ ππππ πΌππΊπ ππ ππ π½πΊππΎ ππ πππΎ ππΊππΎππ ππΎππ ππππ πΊ ππππππΎ πππππΎπ½ ππΎπππΊππΎ!  

<b>π π½πππ πΌππππΊππ½π:</b> 
- /pin: π―ππ πππΎ ππΎπππΊππΎ πππ ππΎππππΎπ½ ππ π¬πΎπππΊππΎ ππ ππΎππ½ πΊ πππππΏππΌπΊππππ ππ πππππ ππΎππ»πΎππ. 
- /unpin: π΄ππππ πππΎ πΌππππΎππ πππππΎπ½ ππΎπππΊππΎ. π¨πΏ πππΎπ½ πΊπ πΊ ππΎπππ, ππππππ πππΎ ππΎππππΎπ½ ππ ππΎπππΊππΎ.
"""
    TGRAPH_TXT ="""<b>π³πΎππΎπππΊππ</b>
π£π πΊπ πππ ππππ ππππ telegra.ph πππ½πππΎ!
<b>π΄ππΊππΎ:</b>

- /telegraph - π²πΎππ½ ππΎ π―ππΌππππΎ ππ π΅ππ½πΎ π΄ππ½πΎπ (π§π¬π‘)

<b>π­π?π³π€:</b>
β’ π²πΊππππΊ ππππππ½ ππΊππΎ πΊπ½πππ ππππππππΊππΎ.
β’ π³πππ π’ππππΊππ½ π¨π π ππΊπππΊπ»ππΎ ππ πππππ πΊππ½ πππ
β’ π³πππ π’ππππΊππ½ π’πΊπ π»πΎ πππΎπ½ π»π πΎππΎπππππΎ
"""
    IMBD_TXT ="""<b>Search</b>
- π²πΎπΊππΌπ πΏπππ π½πΎππΊπππ πππππππ ππΎπΊππππ ππΎππΎπππΊπ
- π²πΎπΊππΌπ πΊπππππππ πππππππ ππΎπΊππππ ππΎππΎπππΊπ
<b>UππΊππΎ:</b>
- /imdb - ππΎπ πππΎ πΏπππ πππΏππππΊππππ πΏπππ π¨π¬π£π» πππππΌπΎ
- /search - ππΎπ πππΎ πΏπππ πππΏππππΊππππ πΏπππ ππΊπππππ πππππΌπΎπ
"""
    INFO_TXT ="""<b>π¨ππΏπ</b>
π¦πΎπ πππΏππππΊππππ πΊπ»πππ ππππΎπππππ!
<b>π΄ππΊππΎ:</b>
β₯ /id - ππΎπ πππΎ ππ½ ππΏ πΊ πππΎπΌππΏπΎπ½ πππΎπ
β₯ /info - ππΎπ πππΎ πππΏππππΊππππ πΊπ»πππ πΊ πππΎπ
"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>
"""
    ADMIN_TXT = """
<b>π€Bot Commands and Usage</b>

β’ /filter ππ /add <code>πΊπ½π½ πΊ πΏππππΎπ</code>
β’ /filters ππ /viewfilters <code>ππππ πΊππ πππΎ πΏππππΎππ ππΏ πΊ πΌππΊπ</code>
β’ /stop ππ /del <code>π½πΎππΎππΎ πΊ πππΎπΌππΏππΌ πΏππππΎπ</code>
β’ /stopall ππ /delall <code>π½πΎππΎππΎ πππΎ πππππΎ πΏππππΎππ ππ πΊ πΌππΊπ</code>
β’ /imdb <code>ππΎπ πππΎ πΏπππ πππΏππππΊππππ πΏπππ π¨π¬π£π» πππππΌπΎ</code>
β’ /search <code>ππΎπ πππΎ πΏπππ πππΏππππΊππππ πΏπππ ππΊπππππ πππππΌπΎπ</code>
β’ /purge <code>π£πΎππΎππΎ πΊππ ππΎπππΊππΎπ Of Groups</code>
β’ /telegraph <code>π²πΎππ½ ππΎ π―ππΌππππΎ ππ π΅ππ½πΎ π΄ππ½πΎπ (π§π¬π‘)</code>
β’ /pin <code>π―ππ πππΎ ππΎπππΊππΎ πππ ππΎππππΎπ½ ππ π¬πΎπππΊππΎ ππ ππΎππ½ πΊ πππππΏππΌπΊππππ ππ πππππ ππΎππ»πΎππ</code>
β’ /unpin <code>π΄ππππ πππΎ πΌππππΎππ πππππΎπ½ ππΎπππΊππΎ</code>
β’ /id <code>ππΎπ πππΎ ππ½ ππΏ πΊ πππΎπΌππΏπΎπ½ πππΎπ</code>
β’ /info <code>ππΎπ πππΎ πππΏππππΊππππ πΊπ»πππ πΊ πππΎπ</code>
β’ /covid [country name] <code>π¦πΎπ πππΏπ πΊπ»πππ πΌππππ½ πΌπΊππΎπ ππ ππππ πΌππππππ</code>
β’ /song [Song Name] <code>π³π ππΎπ πππΎ ππππ</code>
β’ /tr [language code][reply] <code>π³ππΊππππΊππΎ ππΎππππΎπ½ ππΎπππΊππΎ ππ πππΎπΌππΏππΌ ππΊππππΊππΎ.</code>
β’ /Country (Country name) <code>Get info about Country</code>
β’ /stats <code>Get Activities Of Bots</code>
"""
    STATUS_TXT = """π³πππΊπ π₯πππΎπ: <code>{}</code>
π³πππΊπ π¬πΎππ»πΎππ: <code>{}</code>
π³πππΊπ π’ππΊππ: <code>{}</code>
π΄ππΎπ½ π²ππππΊππΎ: <code>{}</code> πΌππ±
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""



    USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
    PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
    PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"
















    START_TXT = """<b>π§α΄ΚΚα΄ {} ππ»ββοΈ
π¬Κ π­α΄α΄α΄ Ιͺs <a href='https://t.me/mcmoviesData2_Bot'>Κα΄Ι΄Ι΄Κα΄.</a> π  π²α΄α΄Κα΄ π±α΄Κα΄α΄ πΆΙͺα΄Κ π¬α΄Ι΄Κ π α΄α΄α΄’ΙͺΙ΄Ι’ π₯α΄α΄α΄α΄Κα΄s. π¨ π’α΄Ι΄ π―Κα΄α΄ Ιͺα΄α΄ π¬α΄α΄ Ιͺα΄s & π§α΄Κα΄ πΈα΄α΄ π³α΄ π¬α΄Ι΄α΄Ι’α΄ πΈα΄α΄Κ π¦Κα΄α΄α΄s, π©α΄sα΄ π α΄α΄ π¬α΄ π³α΄ πΈα΄α΄Κ π¦Κα΄α΄α΄ π s π α΄α΄ΙͺΙ΄ π Ι΄α΄ π€Ι΄α΄α΄Κ.....π₯°</b>
"""
    HELP_TXT = """<b>π§πΎππΎ ππ πππΎ π΄πππΊπ πΌππππΊππ½π</b>: 
/start - πΌππΎπΌπ πππΎπππΎπ ππ ππππππΎ 
/help - ππΎπ ππππ ππΎππ ππΎπππΊππΎ
/about - πΊπ»πππ ππΎ"""
    ABOUT_TXT = """
<b>π€ Κα΄α΄ Ι΄α΄α΄α΄: <a href='https://t.me/mcmoviesData2_Bot'>Κα΄Ι΄Ι΄Κα΄.</a>
π Κα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href='https://www.python.org/'>α΄Κα΄Κα΄Ι΄</a>
π κ°Κα΄α΄α΄α΄‘α΄Κα΄ : <a href='https://github.com/pyrogram/pyrogram'>α΄ΚΚα΄Ι’Κα΄α΄</a>
π‘ Κα΄sα΄α΄α΄ α΄Ι΄ : <a href='http://heroku.com/'>Κα΄Κα΄α΄α΄</a>
π¨βπ» α΄α΄α΄ α΄Κα΄α΄α΄Κ : <a href='https://t.me/iAmLiKu1'>α΄s ΚΙͺα΄α΄ β₯οΈ</a>
π‘ sα΄α΄Κα΄α΄ α΄α΄α΄α΄ : <a href='https://t.me/cs_cloud'>α΄ΚΙͺα΄α΄ Κα΄Κα΄</a>
π₯ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ : <a href='https://t.me/+oMiWi94WoAQ0MmY5'>Mα΄α΄ Ιͺα΄s α΄Κα΄Κ</a>
π’ α΄α΄α΄α΄α΄α΄s α΄Κα΄Ι΄Ι΄α΄Κ : <a href='https://t.me/+tkAjvYxAr7VmZjY1'>α΄α΄ α΄Κα΄Κ</a>
\n\nπ πΈππππ : <code>plz bro credit de dena</code></b>"""
    IMG_TXT = """If You Want To Make A image Of Text send
/hand <anything> to Get the Photo"""

    FONTS_TXT = """ Want Some Stylish fonts send /font <anything>"""

    BOTSTATUS_TXT = """Send /status for getting bot and heroku status"""

    MAMMOKA_TXT = """πππππππ : <b>Iα΄α΄α΄ Fα΄Ι΄s AΚα΄ PΚα΄ΚΙͺΚΙͺα΄α΄α΄ Nα΄α΄Κ TΚΙͺs α΄Κα΄α΄</b> 
    
    <b> πππΌπππ: </b>
    TΚΙͺs ?ΙͺΚα΄α΄Κ α΄α΄Ι΄α΄α΄ΙͺΙ΄s α΄α΄xΙͺα΄ ?α΄Ι΄Ι΄Κ sα΄Ιͺα΄α΄α΄Κs πππ
    
    <b> πΎππππΌππΏ: </b> /ikka βΊβΊ
    
    """

    AUNTY_TXT ="""<b>THE GREAT MALLU AUNTY</b>
   
 Sα΄Ι΄α΄ /aunty, 
 
 TΚα΄Ι΄ Mα΄ΚΚα΄ Aα΄Ι΄α΄Κ WΙͺΚΚ Tα΄xα΄ Yα΄α΄ Sα΄α΄α΄ Jα΄α΄α΄s ππ """

    ABOUTME_TXT = """
<b>π€ Κα΄α΄ Ι΄α΄α΄α΄: <a href='https://t.me/mcmoviesData2_Bot'>Κα΄Ι΄Ι΄Κα΄.</a>
π Κα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href='https://www.python.org/'>α΄Κα΄Κα΄Ι΄</a>
π κ°Κα΄α΄α΄α΄‘α΄Κα΄ : <a href='https://github.com/pyrogram/pyrogram'>α΄ΚΚα΄Ι’Κα΄α΄</a>
π‘ Κα΄sα΄α΄α΄ α΄Ι΄ : <a href='http://heroku.com/'>Κα΄Κα΄α΄α΄</a>
π¨βπ» α΄α΄α΄ α΄Κα΄α΄α΄Κ : <a href='https://t.me/iAmLiKu1'>α΄s ΚΙͺα΄α΄ β₯οΈ</a>
π‘ sα΄α΄Κα΄α΄ α΄α΄α΄α΄ : <a href='https://t.me/cs_cloud'>α΄ΚΙͺα΄α΄ Κα΄Κα΄</a>
π₯ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ : <a href='https://t.me/+oMiWi94WoAQ0MmY5'>Mα΄α΄ Ιͺα΄s α΄Κα΄Κ</a>
π’ α΄α΄α΄α΄α΄α΄s α΄Κα΄Ι΄Ι΄α΄Κ : <a href='https://t.me/+qdq5ZO_xDytkYzJl'>α΄α΄ α΄Κα΄Κ</a>
\n\nπ πΈππππ : <code>plz bro credit de dena</code></b>"""    
    NEXT_TXT = """Welcome To My Second Help Module"""

    NEXTT_TXT = """Welcome To My Third Help Module"""

    WARN_TXT = """Here is the help for the <b>Warns</b> module:

Keep your members in check with warnings; stop them getting out of control!
If you're looking for automated warnings, read about the blacklist module!

<b>Admin Commands</b>:
- /warn <reason>: Warn a user.
- /dwarn <reason>: Warn a user by reply, and delete their message.
- /swarn <reason>: Silently warn a user, and delete your message.
- /warns: See a user's warnings.
- /rmwarn: Remove a user's latest warning.
- /resetwarn: Reset all of a user's warnings to 0.
- /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.
- /warnings: Get the chat's warning settings.
- /setwarnmode <ban/kick/mute>: Set the chat's warn mode.
- /setwarnlimit <number>: Set the number of warnings before users are punished.

<b>Examples</b>
- Warn a user.
-> /warn @user For disobeying the rules"""

    URL_TXT = """Help: <b>URL Shortner</b>
Some URLs is Shortner
<b>Commands and Usage:</b>
β’ /short <code>(link)</code> - I will send the shorted links.
<b>Example:</b>
<code>/short https://t.me/josprojects</code>
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage</b>:
β’ /torrent or /tor : Get Your Torrent Link From Various Resource.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    DISABLE_TXT = """Here is the help for the <b>Disabling</b> module:

This allows you to disable some commonly used commands, so noone can use them. It'll also allow you to autodelete them, stopping people from bluetexting.

<b>Admin commands</b>:
Γ /disable <commandname>: Stop users from using commandname in this group.
Γ /enable <item name>: Allow users from using commandname in this group.
Γ /disableable: List all disableable commands.
Γ /disabledel <yes/no/on/off>: Delete disabled commands when used by non-admins.
Γ /disabled: List the disabled commands in this chat.

<b>Note</b>:
When disabling a command, the command only gets disabled for non-admins. All admins can still use those commands.
Disabled commands are still accessible through the /connect feature. If you would be interested to see this disabled too, let me know in the support chat."""
    
    RULES_TXT = """Here is the help for the <b>Rules</b> module:

Every chat works with different rules; this module will help make those rules clearer!
<b>User commands</b>:
Γ /rules: Check the current chat rules.
<b>Admin commands</b>:
Γ /setrules <text>: Set the rules for this chat.
Γ /privaterules <yes/no/on/off>: Enable/disable whether the rules should be sent in private.
Γ /resetrules: Reset the chat rules to default
Γ /rulesbtn <custom text>: Sets the text of rules button.
Γ /resetrulesbutton: Reset the text of rules button to default.
Γ /resetrulesbtn: Same as above."""

    NOTE_TXT = """Here is the help for the <b>Notes</b> module:

Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!
User commands:
- /get <notename>: Get a note.
- #notename: Same as /get.
<b>Admin commands</b>:
- /save <notename> <note text>: Save a new note called "word". Replying to a message will save that message. Even works on media!
- /clear <notename>: Delete the associated note.
- /notes: List all notes in the current chat.
- /saved: Same as /notes.
- /clearall: Delete ALL notes in a chat. This cannot be undone.
- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM."""
    
    PURGE_TXT = """Here is the help for the <b>Purges</b> module:

<b>Admin only</b>:
- /purge: deletes all messages between this and the replied to message.
- /del: deletes the message you replied to.

<b>Examples</b>:
- Delete all messages from the replied to message, until now.
-> /purge"""

    APPROVE_TXT = """Here is the help for the <b>Approvals</b> module:

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send

<b>User commands</b>:
Γ /approval: Check a user's approval status in this chat.

<b>Admin Commands</b>:
Γ /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
Γ /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
Γ /approved: List all approved users.

<b>Group Owner Commands</b>:
Γ /unapproveall: Unapprove ALL users in a chat. This cannot be undone."""

    LOCK_TXT = """Here is the help for the <b>Locks</b> module:

<b>Admin only</b>:
Γ /lock <permission>: Lock Chat permission..
Γ /unlock <permission>: Unlock Chat permission.
Γ /locks: View Chat permission.
Γ /locktypes: Check available lock types!

Locks can be used to restrict a group's users.
Locking urls will auto-delete all messages with urls, locking stickers will delete all stickers, etc.
Locking bots will stop non-admins from adding bots to the chat.

Example:
/lock media: this locks all the media messages in the chat."""
    FILE_TXT = """β€ πππ₯π©: ππ’π₯π ππ­π¨π«π ππ¨ππ?π₯π../

<b>By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files files.../</b>

βͺΌ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π βΊ

βͺ /plink βΊβΊ <b>π±πΎπππ ππ πΊππ ππΎπ½ππΊ ππ ππΎπ ππππ.</b>
βͺ /pbatch βΊβΊ <b>π΄ππΎ ππππ πeπ½ππΊ ππππ ππππ ππππ πΌππππΊππ½.</b>
βͺ /batch βΊβΊ <b>To Create Link For Multiple Post.</b>

βͺΌ ππ±ππ¦π©π₯π βΊ

<code>/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336</code>"""

    WELCOME_TXT ="""Here is the help for the <b>Greetings</b> module:

Welcome new members to your groups or say Goodbye after they leave!

<b>Admin Commands</b>:
Γ /setwelcome <reply/text>: Sets welcome text for group.
Γ /welcome <yes/no/on/off>: Enables or Disables welcome setting for group.
Γ /resetwelcome: Resets the welcome message to default.
Γ /setgoodbye <reply/text>: Sets goodbye text for group.
Γ /goodbye <yes/no/on/off>: Enables or Disables goodbye setting for group.
Γ /resetgoodbye: Resets the goodbye message to default.
Γ /cleanservice <yes/no/on/off>: Delete all service messages such as 'x joined the group' notification.
Γ /cleanwelcome <yes/no/on/off>: Delete the old welcome message, whenever a new member joins."""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
β’/whois :-give a user full details"""
    FUN_TXT ="""<b>Gα΄α΄α΄s</b> 
    
<b>π² NOTHING MUCH JUST SOME FUN THINGS</b>
tππ ππππ π?ππ: 
π£. /dice - Roll The Dice 
π€. /Throw ππ /Dart - π³π π¬πΊππΎ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    ENGLISH_TXT = """HELP:English
 β /define <text>*:* TΚα΄α΄ α΄Κα΄ α΄‘α΄Κα΄ α΄Κ α΄xα΄Κα΄ssΙͺα΄Ι΄ Κα΄α΄ α΄‘α΄Ι΄α΄ α΄α΄ sα΄α΄Κα΄Κ\Ι΄Fα΄Κ α΄xα΄α΄α΄Κα΄ /define α΄ΙͺΚΚ
 β /spell*:* α΄‘ΚΙͺΚα΄ Κα΄α΄ΚΚΙͺΙ΄Ι’ α΄α΄ α΄ α΄α΄ssα΄Ι’α΄, α΄‘ΙͺΚΚ Κα΄α΄ΚΚ α΄‘Ιͺα΄Κ α΄ Ι’Κα΄α΄α΄α΄Κ α΄α΄ΚΚα΄α΄α΄α΄α΄ α΄ α΄ΚsΙͺα΄Ι΄
 β /synonyms <word>*:* FΙͺΙ΄α΄ α΄Κα΄ sΚΙ΄α΄Ι΄Κα΄s α΄? α΄ α΄‘α΄Κα΄
 β /antonyms <word>*:* FΙͺΙ΄α΄ α΄Κα΄ α΄Ι΄α΄α΄Ι΄Κα΄s α΄? α΄ α΄‘α΄Κα΄
"""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>
a bot to create a link to share text in the telegram.
<b>Commands and Usage:</b>
β’ /share (text or reply to message)
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    SOURCE_TXT = """<b>Source:</b>
This bot is a Close source project.But my source code would be here
Source: <a href='https://Github.com/EvaMariaTG/EvaMaria'>Source - Click here π</a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and α©αα©α­  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. α©αα©α­ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>πΌSong DownloadπΌ</b>
Song Download Module, For Those Who Love Music

<b>π Command π</b>

- /song [Song Name] - To Download Music π

<b>πUsageπ</b>
- Can Be Used By Everyone
- Works in bot pm

Made By <a href=https://t.me/+veUIdIW2CQ5mOGU5>ππ ππ©πππ­ππ¬</a>"""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>
a bot to create a link to share text in the telegram.
<b>Commands and Usage:</b>
β’ /share (text or reply to message)
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
   
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>π Commands & Usage:</b>

β /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
β /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

β’ /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS π€ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

β’ /tts <text> : convert text to speech

<b>NOTE:</b>

β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>π Ping:</b>

Helps you to know your ping πΆπΌββοΈ

<b>Commands:</b>

β’ /alive - To check you are alive.
β’ /help - To get help 
β’ /ping - To get your ping 
β’ /repo - Source Code. 

<b>πΉUsageπΉ :</b>

β’ This commands can be used in pms and groups
β’ This commands can be used buy everyone in the groups and bots pm
β’ Share us for more features"""
    TELE_TXT = """<b>β«οΈHELP: TelegraphβͺοΈ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

π€§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

β’ This Command Is Available in goups and pms
β’ This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>π£Purgeπ£</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

β /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-α©αα©α­  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. α©αα©α­ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+veUIdIW2CQ5mOGU5)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of α©αα©α­ 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban_user  - <code>to ban a user.</code>
β’ /unban_user  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>βͺ <b>Total Files:</b> <code>{}</code>
βͺ <b>Total Users:</b> <code>{}</code>
βͺ <b>Total Chats:</b> <code>{}</code>
βͺ <b>Used Storage:</b> <code>{}</code> 
βͺ <b>Free Storage:</b> <code>{}</code> """
    LOG_TEXT_G = """#πππ°ππ«π¨π?π©
    
Group = @{} (<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#πππ°ππ¬ππ«
    
<b>αβΊ ππ - <code>{}</code></b>
<b>αβΊ πππ¦π - {}</b>
"""
    REPORT_TXT = """β€ πππ₯π©: Rα΄α΄α΄Κα΄ β οΈ

ππππ πππππππ πππππ π’ππ ππ ππππππ π πππππππ ππ π ππππ ππ πππ ππππππ ππ πππ ππππππππππ πππππ. π³ππ'π ππππππ ππππ πππππππ.

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ/report ππ @admins - π³π ππΎππππ πΊ πππΎπ ππ πππΎ πΊπ½ππππ (ππΎπππ ππ πΊ ππΎπππΊππΎ)."""

    CORONA_TXT = """β€ πππ₯π©: π’ππππ½

ππππ π²ππππππ πππππ π’ππ ππ ππππ  πππππ’ πππππππππππ πππππ πππππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /covid - πππΎ ππππ πΌππππΊππ½ ππππ ππππ πΌππππππ ππΊππΎ ππ ππΎπ πΌππππ½πΎ πππΏππππΊππππ

βπ€ππΊππππΎ:
/covid π¨ππ½ππΊ"""

    URLSHORT_TXT = """β€ πππ₯π©: π΄ππ πππππππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππ π πππ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /short: πππΎ ππππ πΌππππΊππ½ ππππ ππππ ππππ ππ ππΎπ ππππππΎπ½ πππππ

βπ€ππΊππππΎ:
/short https://t.me/+veUIdIW2CQ5mOGU5"""

    VIDEO_TXT ="""π·π΄π»πΏ ππΎπ ππΎ π³πΎππ½π»πΎπ°π³ ππΈπ³π΄πΎ π΅ππΎπΌ ππΎππππ±π΄.

β’ ππ΄π’π¨π¦
π π°πΆ ππ’π― ππ°πΈπ―π­π°π’π₯ ππ―πΊ ππͺπ₯π¦π° ππ³π°π? π π°πΆπ΅πΆπ£π¦

ππ€π¬ ππ€ ππ¨π
β’ ππΊπ±π¦ /video or /mp4 ππ―π₯ (ππͺπ₯π¦π° Link)
β’ ππΉπ’π?π±π­π¦:
/π?π±4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """π·π΄π»πΏ ππΎπ ππΎ πΊπΈπ²πΊ πππ΄ππ

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """β€ πππ₯π©: Iα΄α΄Ι’α΄

ππππ πππππππ πππππ π’ππ ππ ππππ πππππ ππππ’ ππππππ’ 

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ π©πππ ππΎππ½ ππΎ πΊ πππΊππΎ ππ πΎπ½ππ β¨

π¬πΊπ½πΎ π»π <a href=https://t.me/+veUIdIW2CQ5mOGU5>ππ ππ©πππ­ππ¬</a>"""

    STICKER_TXT = """ππΎπ π²π°π½ πππ΄ ππ·πΈπ πΌπΎπ³ππ»π΄ ππΎ π΅πΈπ½π³ π°π½π πππΈπ²πΊπ΄ππ πΈπ³.
β’ πππππ
To Get Sticker ID
 
  β­ ππ€π¬ ππ€ ππ¨π
 
β Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """π·π΄π»πΏπ ππΎ π³πΎππ½π»πΎπ°π³ π°π½π ππΎππππ±π΄ ππΈπ³π΄πΎ ππ·ππΌπ±π½π°πΈπ»
    
β­ππ€π¬ ππ€ ππ¨π
ππΊπ±π¦ /ytthumb ππ―π₯ ππͺπ₯π¦π° ππͺπ―π¬

β’ ππΉπ’π?π±π­π¦
/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """β€ πππ₯π©: π ππ½πππ»πππ

πππ πππ πππππππ π πΏπ³π΅ ππππ ππ π πππππ ππππ π πππ ππππ πππππππ β―

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ /audiobook: π±πΎπππ ππππ πΌππππΊππ½ ππ πΊππ π―π£π₯ ππ ππΎππΎππΊππΎ πππΎ πΊππ½ππ"""

    GTRANS_TXT = """β€ πππ₯π©: π¦πππππΎ π³ππΊππππΊππΎπ

ππππ πππππππ πππππ π’ππ ππ πππππππππ π πππ‘π ππ πΊππ πππππππππ π’ππ π πππ. ππππ πππππππ π ππππ ππ ππππ ππ πππ πππππ β―

β€ ππ¨π¦π¦ππ§ππ¬ ππ§π ππ¬ππ π:

βͺ/tr - π³π πππΊππππΊππΎπ ππΎπππ ππ πΊ πππΎπΌππΏπΌ ππΊππππΊππΎ

β€ π­πππΎ:
πΆππππΎ πππππ /tr πππ ππππππ½ πππΎπΌππΏπ πππΎ ππΊππππΊππΎ πΌππ½πΎ

βπ€ππΊππππΎ: /ππ ππ
β’ πΎπ = π€ππππππ
β’ ππ = π¬πΊππΊππΊππΊπ
β’ ππ = π§πππ½π"""

    RESTRIC_TXT = """β€ πππ₯π©: Mα΄α΄α΄ π«

πππππ πππ πππ ππππππππ π πππππ πππππ πππ πππ ππ ππππππ πππππ πππππ ππππ πππππππππππ’.

βͺ/ban: π³π π»πΊπ πΊ πππΎπ πΏπππ πππΎ πππππ.
βͺ/unban: π³π πππ»πΊπ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tban: π³π ππΎπππππΊππππ π»πΊπ πΊ πππΎπ.
βͺ/mute: π³π ππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/unmute: π³π ππππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tmute: π³π ππΎπππππΊππππ ππππΎ πΊ πππΎπ.

β€ π­πππΎ:
πΆππππΎ πππππ /tmute ππ /tban πππ ππππππ½ πππΎπΌππΏπ πππΎ ππππΎ πππππ.

βπ€ππΊππππΎ: /ππ»πΊπ 2π½ ππ /πππππΎ 2π½.
πΈππ πΌπΊπ πππΎ ππΊπππΎπ: π/π/π½. 
 β’ π = ππππππΎπ
 β’ π = πππππ
 β’ π½ = π½πΊππ"""
    CREATOR_REQUIRED = """β<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """π? Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """β<b>ΰ΄ΰ΄¨ΰ΅ΰ΄¨ΰ΅ Admin ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄€ΰ΅ΰ΄€ ΰ΄Έΰ΅ΰ΄₯ΰ΄²ΰ΄€ΰ΅ΰ΄€ΰ΅ ΰ΄ΰ΄Ύΰ΅» ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄² ΰ΄ͺΰ΅ΰ΄ΰ΅ΰ΄΅ΰ΄Ύ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ΰ΄ΰ΄ͺΰ΅ΰ΄ͺΰ΅ ΰ΄ΰ΄²ΰ΅ΰ΄²ΰ΄Ύΰ΄ ΰ΄ΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ΰ΄?ΰ΄Ύΰ΄±ΰ΅ΰ΄±ΰ΄Ώ ΰ΄€ΰ΄°ΰ΄Ύΰ΄...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
