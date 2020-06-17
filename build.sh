export PATH=~/.local/bin/:$PATH
buildozer android release
cd  ~/calculmental/bin/
#wget nas/certificatsAPK/calculmental-key.keystore
#keytool -genkey -v -keystore calculmental-key.keystore -alias calculmental-alias -keyalg RSA -keysize 2048 -validity 25000
apksigner sign --ks calculmental-key.keystore --in CalculMentalapp-0.1-arm64-v8a-release-unsigned.apk --out calculMental-sign.apk
