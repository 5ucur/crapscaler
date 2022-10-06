# crapscaler
 what a crappy upscaler!
 
 A crappy image upscaler. Don't use it. Written in less than two days. I think I spent more time on this readme than on the program.  
 Inspiration came from pondering audio files, actually, one day when there was a power outage.   
 Absolutely zero research on upscaling has been done for this program.   
 Crapscaler does not use AI, blockchain, NFT, ML, DL, or any other technology buzzword. It is unoptimised, but lightweight in requirements.   
 This readme has been formatted for GitHub's flavour of Markdown. Elsewhere, it may look different from what was intended, especially the mathematical expressions.
 
-----
## How it works
 Crapscaler works on the concept of finding averages between all adjacent pairs of elements in an array of length $n$, and inserting them appropriately, resulting in a $2n-1$ long array.   
 The program does this to the rows of an image first, then transposes, does the same to the columns (now rows, after transposing), and transposes back, resulting in an image of size $(2x-1) * (2y-1)$, where $x$ and $y$ are the dimensions of the original image. All floating-point values are rounded in the process of crapscaling an image.
 
 To illustrate with simple numbers instead of colours (without rounding):

 input:   
 ```
 [   
    [1, 2],   
    [3, 4]   
 ]
 ```   
 first run:   
 ```
 [   
    [1, 1.5, 2],   
    [3, 3.5, 4]   
 ]
 ```   
 transposed:   
 ```
 [   
    [1,   3],   
    [1.5, 3.5],   
    [2,   4]   
 ]
 ```   
 second run:   
 ```
 [   
    [1,   2,   3],   
    [1.5, 2.5, 3.5],   
    [2,   3,   4]   
 ]
 ```   
 transpose back:   
 ```
 [   
    [1, 1.5, 2],   
    [2, 2.5, 3],   
    [3, 3.5, 4]   
 ]
 ```
 --------
 ## Some maths
 Because ${a + b \over 2} + {c + d \over 2} = {a + c \over 2} + {b + d \over 2} = {a + b + c + d \over 2}$,   
 and indeed ${{a + b \over 2} + {c + d \over 2} \over 2} = {{a + c \over 2} + {b + d \over 2} \over 2} = {{a + b + c + d \over 2} \over 2} = {a + b + c + d \over 4}$,   
 it does not matter if the value in the centre between four corners is determined between two adjacent values in a row, two adjacent values in a column, or all four.   
 In other words, in our example,   
 ${{1 + 2 \over 2} + {3 + 4 \over 2} \over 2} = {1.5 + 3.5 \over 2} = {5 \over 2} = 2.5$   
 ${{1 + 3 \over 2} + {2 + 4 \over 2} \over 2} = {2 + 3 \over 2} = {5 \over 2} = 2.5$   
 ${1 + 2 + 3 + 4 \over 4} = {10 \over 4} = 2.5$   
 and even   
 ${1.5 + 3.5 + 2 + 3 \over 4} = {10 \over 4} = 2.5$   
 But the value has been determined using only ${1.5 + 3.5 \over 2}$ as one method is enough and that one came up in the algorithm.
 
 -----
 ## How to use
 Don't.
 ### How to use?????!!!!!
 Okay...    
 `python3 crapscaler.py /path/to/image/file.extension`   
 For example,  
 `python3 crapscaler.py /home/bob/cat.png`

 The output file will be saved in the same directory as the input file, with a modified filename to mention it has been crapscaled, as well as with the date and time (to the second) when it was crapscaled. Example:   
 `/home/bob/cat_crapscaled_2022_12_31_14_15_16.png` would be done on Dec 31. 2022. at 2:15:16 PM.
 
 If you're certain your `python` is `python3`, you can omit the `3`. Maybe it even works properly in Python 2. Haven't tested.   
 Does not work for .gif. Have tested with .jpg and .png, works for those. May work for some other filetypes. Supports transparency in .png.   
 Absolutely nothing is guaranteed. I told you not to use it. It's on you if it doesn't work or screws something up. This is also in the license.
