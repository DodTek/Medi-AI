package com.example.mediai2.ui.main;

import android.util.Log;

import androidx.arch.core.util.Function;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.Transformations;
import androidx.lifecycle.ViewModel;

import com.example.mediai2.R;
import com.example.mediai2.Tabs;

public class PageViewModel extends ViewModel {

    private MutableLiveData<Integer> mIndex = new MutableLiveData<>();
    private LiveData<String> mText = Transformations.map(mIndex, new Function<Integer, String>() {
        @Override
        public String apply(Integer input) {
            String s = null;
            switch (input){
                    case 1:
                        s = "Please input your information below to check your risk of cancer" ;
                        break;
                    case 2:
                        s = "Please input your information below to check your risk of diabetes";
                        break;
                    case 3:
                        s =  "Please input your information below to check your risk of heart disease";
                        break;
                    case 4:
                        s = "Support";
                        break;
                }
         return s;
        }
    });

    public void setIndex(int index) {
        mIndex.setValue(index);
    }

    public LiveData<String> getText() {
        return mText;
    }
}