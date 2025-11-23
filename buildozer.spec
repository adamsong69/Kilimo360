[app]
title = TARI_Kilimo360
package.name = kilimo360
package.domain = tz.tari
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt
version = 0.2
requirements = python3,kivy==2.2.0,kivymd==1.1.1,kivy_garden.mapview,plyer
orientation = portrait
icon.filename = %(source.dir)s/assets/icons/icon.png
presplash.filename = %(source.dir)s/assets/icons/presplash.png
android.api = 33
android.ndk = 25b
android.minapi = 21
android.archs = armeabi-v7a
android.permissions = INTERNET,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
