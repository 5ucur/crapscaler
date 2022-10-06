# crapscaler
 what a crappy upscaler!
 
 A crappy image upscaler. Don't use it. Written in less than two days.   
 Inspiration came from pondering audio files, actually, one day when there was a power outage.   
 Absolutely zero research on upscaling has been done while writing this program.

## How it works
 Crapscaler works on the concept of finding averages between all adjacent pairs elements in an array of length n, and inserting them appropriately, resulting in a 2n-1 long array.   
 The program does this to the rows of an image first, then transposes, does the same to the columns (now rows, after transposing), and transposes back.   
 To illustrate with simple numbers instead of colours:

 input:   
 `[`   
 `   [1, 2],`   
 `   [3, 4]`   
 `]`   
 first run:   
 `[`   
 `   [1, 1.5, 2],`   
 `   [3, 3.5, 4]`   
 `]`   
 transposed:   
 `[`   
 `   [1,   3],`   
 `   [1.5, 3.5],`   
 `   [2,   4]`   
 `]`   
 second run:   
 `[`   
 `   [1,   2,   3],`   
 `   [1.5, 2.5, 3.5],`   
 `   [2,   3,   4]`   
 `]`   
 transpose back:   
 `[`   
 `   [1, 1.5, 2],`   
 `   [2, 2.5, 3],`   
 `   [3, 3.5, 4]`   
 `]`   
 
 Because   
 $$ {{a + b \over 2} + {c + d \over 2} \over 2} = {{a + b + c + d \over 2} \over 2}$$,   
 it does not matter if the value in the centre between four corners is determined between two adjacent values in a row or two adjacent values in a column.   
 In other words, in our example, $2.5 = {1.5 + 3.5 \over 2} = {2 + 3 \over 2}$.
