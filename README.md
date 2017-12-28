## spd
An easy way to manage your wallpaper in Mac!
Search, download an image and set it as your wallpaper in one cmd!

### Requirements 
- scrapy

    you can install scrapy via pip

    ```
    pip install scrapy
    ```

- wget

### Installation
just run the following command.

```
git clone https://github.com/WangsirCode/spd.git ~/.spd && cd ~/.spd && make
```

### Usage
To grab an image and set it as your wallpaper, just run:

```
spdstart
```
It will crawl an image from [simple desktop](http://simpledesktops.com/) and set it as your wallpaper automatically.

it also support [hdwallpapers](https://www.hdwallpapers.in) and [wallhaven](https://alpha.wallhaven.cc), to grab image from these websites just run

```
spdstart hdwallpapers  or spdstart wallhaven
```




