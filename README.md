# pylambda
python lambda scripting with images inspired by mnhrdt/imscript plambda


## dependencies

    pip install iio numpy


## usage

operate with two images to compute `output.tiff`

    ./pylambda.py image1.tiff image2.tiff "sqrt(x**2 + y**2)" -o output.tiff

or just visualize the result

    ./pylambda.py image1.tiff image2.tiff "sqrt(x**2 + y**2)" | vpv
    
