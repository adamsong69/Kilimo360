[app]
title = Kilimo360
package.name = kilimo360
package.domain = org.example
source.include_exts = py,png,jpg,kv,json,txt
version = 0.2
requirements = python3,kivy==2.2.0,kivymd==1.1.1,kivy_garden.mapview,plyer
android.api = 33
android.ndk = 25b
android.minapi = 21
android.arch = armeabi-v7a
android.permissions = INTERNET,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,RECORD_AUDIO,ACCESS_COARSE_LOCATION
orientation = portrait
presplash.filename = %(source.dir)s/assets/icons/presplash.png

[buildozer]
log_level = 2
