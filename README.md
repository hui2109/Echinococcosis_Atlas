# Echinococcosis_Atlas

## 打包指令

### windows
nuitka --standalone --include-data-dir=./asset=./asset --output-dir=o --enable-plugin=pyside6 --disable-console --windows-icon-from-ico=./asset/disease.png ./main_call.py

### macos

nuitka3 --standalone --include-data-dir=./asset=./asset --output-dir=o --enable-plugin=pyside6 --disable-console --macos-create-app-bundle --macos-app-icon=./asset/disease.png ./main_call.py

