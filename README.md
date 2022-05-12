# SPROJ_LUMS

#### Data

- reports/ include individual CSV files for ~1000 Alexa Popular webpages which summarizes all the requests made for images (image names), their transfer, actual and optimized sizes.
- Images for Alexa-1000 webpages and their optimized versions can be made available upon request (Total size exceeds 5GB).




*Note: In some summaries, you may come across images with transfer and actual sizes equal to 0 (request was made but the resource failed to be fetched), however, their optimized sizes are not 0. It is because of the possibility of image being successfully downloaded but not loaded when the network trace was captured by lighthouse (Both done in separate runs). In some cases, different images of a webpage had same names leading to discrepancy in mapping optimized sizes to it. Images with such issues were never used in calculations of data savings. Hence, we never overestimate data savings.*