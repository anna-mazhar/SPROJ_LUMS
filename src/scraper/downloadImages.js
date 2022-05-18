import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
import path from 'path';
import fs from 'fs'
import { exec } from 'child_process';

(async () => {


  let url = ''

  if (typeof process.argv[2] == "undefined") {
    console.log('Error: Please add a URL in the arguments')
    process.exit()
  }

  url = process.argv[2]


  puppeteer.use(StealthPlugin());

  const browser = await puppeteer.launch({
      headless : false, 
      defaultViewport: {width: 360, height: 640, isMobile: true, hasTouch: true},  
      args: ['--start-maximized', '--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'] 

  });
 
  let url_file_name = url.replace('https://www.','')
  url_file_name = url_file_name.replace('.','-')
  url_file_name = url_file_name.replace('/','')

  try {

    const page = await browser.newPage();
    const session = await page.target().createCDPSession();

    if (fs.existsSync('images/')) {
        fs.rmdirSync('images/', {recursive: true})
        fs.mkdirSync("images/")
    } 
    else
    fs.mkdirSync("images/")
    let c = 1

    page.on('response', async(response) => {


        // accept response with status code between 199 and 300 (response with a body) 
        // ignore response with status code 204 (response status with 204 has no content) 
        if(response.status() != 204 && response.status() > 199 && response.status() < 300){


            if (response.request().resourceType() === 'image') {
                
                await response.buffer().then(file => {
                  
                    if (file.length != 0){

                      
                        c += 1
                        
                        let fileName = path.basename(response.url())
                        fileName = fileName.substring(0,200).split(',')   // limit filename length acc to OS limit which is 255
                        fileName = fileName.join('')
                        let filePath = ''
                        
                        filePath = path.resolve('images/', fileName);
                        const writeStream = fs.createWriteStream(filePath);
                        writeStream.write(file);
                    } 
                });
                
                
            }

        }

    });


    await page.goto(url , {
    waitUntil: 'load',  //with networkidle0 some pages would never fulfill this condition and would never close
    timeout: 0
    });


    await session.send('Input.synthesizeScrollGesture', {
      x: 100,
      y: 0,
      yDistance: -8000,
      speed: 500, // 1000
      repeatCount: 0,
      repeatDelayMs: 250,
      gestureSourceType: "mouse"
    });

    await page.close()

  } catch (e) {

    console.log("Error: ", e)

  } finally {

    await browser.close();
    
  }


  exec("python3 to_webp.py " + url, (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`${stdout}`);
  });



})();
  
