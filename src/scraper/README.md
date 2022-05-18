# Downloading Images

We use Puppeteer to simulate a mobile device page load, download requested resources (we require only images in this case so we filter out images) and perform automated scrolling to download the lazy loaded resources as well.

After cloning the repository:

- Install dependencies:

```sh
npm install
```

- Run the scraper:

```sh
node downloadImages.js https://www.amazon.com
```
It will download all the requested images and will perform image optimizations including conversion to WebP and image compression.

The downloaded resources can be found under 'code/scraper/images/'. 
- Images converted to WebP will be found under 'code/scraper/images/75/'
- Compressed version with quality factor 50 will be found under 'code/scraper/images/50/'
- Compressed version with quality factor 30 will be found under 'code/scraper/images/30/'
and so on..
<br>

Try the following example webpages:
```sh
node downloadImages.js https://www.naver.com
```
```sh
node downloadImages.js https://www.alibaba.com
```
```sh
node downloadImages.js https://www.nytimes.com
```
<br>

