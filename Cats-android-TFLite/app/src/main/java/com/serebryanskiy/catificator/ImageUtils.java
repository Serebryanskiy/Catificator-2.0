package com.serebryanskiy.catificator;

import android.graphics.Bitmap;
import android.graphics.ColorMatrix;

public class ImageUtils {

    public static Bitmap prepareImageForClassification(Bitmap bitmap) {
        Bitmap bmpGrayscale = Bitmap.createScaledBitmap(
                bitmap,
                CatsModelConfig.INPUT_IMG_SIZE_WIDTH,
                CatsModelConfig.INPUT_IMG_SIZE_HEIGHT,
                false);
        return bmpGrayscale;
    }

}
