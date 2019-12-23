package com.example.mediai2;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.mediai2.ui.main.SectionsPagerAdapter;
import com.google.android.material.tabs.TabLayout;
import org.json.JSONException;
import org.json.JSONObject;

public class Tabs extends AppCompatActivity {
    private Response.Listener listener;
    public String email;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Bundle  bundle = getIntent().getExtras();
        assert bundle != null;
        email = bundle.getString("username");
        setContentView(R.layout.activity_tabs);
        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager());
        ViewPager viewPager = findViewById(R.id.view_pager);
        viewPager.setAdapter(sectionsPagerAdapter);
        TabLayout tabs = findViewById(R.id.tabs);
        tabs.setupWithViewPager(viewPager);
    }
    public void makePredictionCancer(View view) {
        try {
            EditText age = findViewById(R.id.cancerAgeTextField);
            EditText bmi = findViewById(R.id.cancerBMITextField);
            EditText glucose = findViewById(R.id.cancerGluxcoseTextField);
            EditText insulin = findViewById(R.id.cancerInsulinTextField);
            EditText homa = findViewById(R.id.cancerHomaTextField);
            EditText leptin = findViewById(R.id.cancerLeptinTextField);
            EditText adi = findViewById(R.id.cancerAdiTextField);
            EditText rest = findViewById(R.id.cancerResTextField);
            EditText mcp = findViewById(R.id.cancerMcpTextField);

            String ageString  = age.getText().toString();
            String bmiString  = bmi.getText().toString();
            String glucoseString  = glucose.getText().toString();
            String insulinString  = insulin.getText().toString();
            String homaString  = homa.getText().toString();
            String leptinString  = leptin.getText().toString();
            String adiString  = adi.getText().toString();
            String restString  = rest.getText().toString();
            String mcpString  = mcp.getText().toString();

            JSONObject cancerInfo = new JSONObject();
            cancerInfo.put("user_email", email);
            cancerInfo.put("Age", ageString);
            cancerInfo.put("BMI",bmiString);
            cancerInfo.put("Glucose", glucoseString);
            cancerInfo.put("Insulin", insulinString);
            cancerInfo.put("HOMA", homaString);
            cancerInfo.put("Leptin", leptinString);
            cancerInfo.put ("Adiponectin", adiString);
            cancerInfo.put("Resistin", restString);
            cancerInfo.put("MCP-1",mcpString);

           // System.out.println(cancerInfo.toString());
            final String url = "http://mp00152561.pythonanywhere.com/cancer_api";
            RequestQueue requestQueue = Volley.newRequestQueue(Tabs.this);

            final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,cancerInfo, new Response.Listener<JSONObject>() {

                @Override//response from the website
                public void onResponse(JSONObject response) {
                    try {
                        response.get("prediction");
                        System.out.println(response.get("prediction"));
                        if(response.get("prediction").equals("0")){
                            Toast.makeText(Tabs.this,"It is unlikely that you have breast cancer.", Toast.LENGTH_SHORT).show();
                        }
                        else {
                            Toast.makeText(Tabs.this,"You may have breast cancer. Please consult your GP", Toast.LENGTH_SHORT).show();
                        }

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    System.out.println(response);
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    if(listener!=null){
                        error.getCause();
                    }
                }
            });

          requestQueue.add(stringRequest);
        }
        catch(Exception e){
            e.printStackTrace();
        }

    }
    public void makePredictionHeart(View view) {
        try {
            EditText age = findViewById(R.id.heartTextFieldAge);
            EditText sex = findViewById(R.id.heartTextFieldSex);
            EditText chest = findViewById(R.id.heartTextFieldCp);
            EditText trest = findViewById(R.id.heartTextFieldTrest);
            EditText chol = findViewById(R.id.heartTextFieldChol);
            EditText fbs = findViewById(R.id.heartTextFieldFbs);
            EditText rest = findViewById(R.id.heartTextFieldRest);
            EditText thalach = findViewById(R.id.heartTextFieldThalach);
            EditText exang = findViewById(R.id.heartTextFieldExang);
            EditText oldpeak = findViewById(R.id.heartTextFieldOldpeak);
            EditText slope = findViewById(R.id.heartTextFieldSlope);
            EditText ca = findViewById(R.id.heartTextFieldCa);
            EditText thal = findViewById(R.id.heartTextFieldThal);

            String ageString  = age.getText().toString();
            String sexString  = sex.getText().toString();
            String chestString  = chest.getText().toString();
            String trestString  = trest.getText().toString();
            String cholString  = chol.getText().toString();
            String fbsString  = fbs.getText().toString();
            String restString  = rest.getText().toString();
            String thalachString  = thalach.getText().toString();
            String exangString  = exang.getText().toString();
            String oldpeakString  = oldpeak.getText().toString();
            String slopeString  = slope.getText().toString();
            String caString  = ca.getText().toString();
            String thalString  = thal.getText().toString();

            JSONObject heartInfo = new JSONObject();
            heartInfo.put("user_email", email);
            heartInfo.put("age", ageString);
            heartInfo.put("sex",sexString);
            heartInfo.put("cp", chestString);
            heartInfo.put("trestbps", trestString);
            heartInfo.put("chol", cholString);
            heartInfo.put("fbs", fbsString);
            heartInfo.put("restecg", restString);
            heartInfo.put ("thalach", thalachString);
            heartInfo.put("exang", exangString);
            heartInfo.put("oldpeak",oldpeakString);
            heartInfo.put("slope",slopeString);
            heartInfo.put("ca",caString);
            heartInfo.put("thal",thalString);

            System.out.println(heartInfo.toString());
            System.out.println(heartInfo);
            final String url = "http://mp00152561.pythonanywhere.com/heartdisease_api";
            RequestQueue requestQueue = Volley.newRequestQueue(Tabs.this);

            final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,heartInfo, new Response.Listener<JSONObject>() {

                @Override
                public void onResponse(JSONObject response) {
                    try {
                        response.get("prediction");
                        System.out.println(response.get("prediction"));
                        if(response.get("prediction").equals("0")){
                            Toast.makeText(Tabs.this,"It is unlikely that you have heart disease.", Toast.LENGTH_SHORT).show();
                        }
                        else {
                            Toast.makeText(Tabs.this,"You may have heart disease. Please consult your GP", Toast.LENGTH_SHORT).show();
                        }

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    System.out.println(response);
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    if(listener!=null){
                        error.getCause();
                    }
                }
            });

            requestQueue.add(stringRequest);
        }
        catch(Exception e){
            e.printStackTrace();
        }

    }
    public void makePredictionDiabetes(View view) {
        try {
            EditText age = findViewById(R.id.diabetesAgeTextField);
            EditText bmi = findViewById(R.id.diabetesBmiTextField);
            EditText insulin = findViewById(R.id.diabetesInsulinTextField);
            EditText ped = findViewById(R.id.diabetesPedigreeTextField);
            EditText thick = findViewById(R.id.diabetesSkinTextField);
            EditText glucose = findViewById(R.id.diabetesGlucoseTextField);
            EditText pregnancy = findViewById(R.id.diabetesPregnancyTextField);
            EditText pressure = findViewById(R.id.diabetesBloodTextField);

            String ageString  = age.getText().toString();
            String bmiString  = bmi.getText().toString();
            String insulinString  = insulin.getText().toString();
            String pedString  = ped.getText().toString();
            String thickString  = thick.getText().toString();
            String glucoseString  = glucose.getText().toString();
            String pregnancyString = pregnancy.getText().toString();
            String pressureString = pressure.getText().toString();

            JSONObject diabetesInfo = new JSONObject();
            diabetesInfo.put("user_email", email);
            diabetesInfo.put("Pregnancies", pregnancyString);
            diabetesInfo.put("Glucose", glucoseString);
            diabetesInfo.put("BloodPressure", pressureString);
            diabetesInfo.put("SkinThickness", thickString);
            diabetesInfo.put("Insulin", insulinString);
            diabetesInfo.put("BMI",bmiString);
            diabetesInfo.put("DiabetesPedigreeFunction", pedString);
            diabetesInfo.put("AgeYears", ageString);

            System.out.println(diabetesInfo.toString());
            final String url = "http://mp00152561.pythonanywhere.com/diabetes_api";
            RequestQueue requestQueue = Volley.newRequestQueue(Tabs.this);

            final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,diabetesInfo, new Response.Listener<JSONObject>() {

                @Override
                public void onResponse(JSONObject response) {
                    try {
                        response.get("prediction");
                        System.out.println(response.get("prediction"));
                        if(response.get("prediction").equals("0")){
                            Toast.makeText(Tabs.this,"It is unlikely that you have diabetes.", Toast.LENGTH_SHORT).show();
                        }
                        else {
                            Toast.makeText(Tabs.this,"You may have diabetes. Please consult your GP", Toast.LENGTH_SHORT).show();
                        }

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    System.out.println(response);
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    if(listener!=null){
                        error.getCause();
                    }
                }
            });

            requestQueue.add(stringRequest);
        }
        catch(Exception e){
            e.printStackTrace();
        }

    }

    public void getPredictions(View view) throws JSONException {
        JSONObject user = new JSONObject();
        final TextView diabetes = findViewById(R.id.supportTextView1);
        final TextView cancer = findViewById(R.id.supportTextView2);
        final TextView heart = findViewById(R.id.supportTextView3);


        final String url = "http://mp00152561.pythonanywhere.com/get_details";
        final RequestQueue requestQueue = Volley.newRequestQueue(Tabs.this);
        user.put("email",email);

        final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,user, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {
                try {
                    if(response.get("diabetes").equals("1")){
                        //fill text view
                        diabetes.setText("Chance of diabetes: 1");
                    }
                    else {
                        diabetes.setText("Chance of diabetes: 0");

                    }
                    if(response.get("cancer").equals("1")){
                        //fill text view
                        cancer.setText("Chance of breast cancer: 1");
                    }
                    else {
                        cancer.setText("Chance of breast cancer: 0");
                    }
                    if(response.get("heart_disease").equals("1")){
                        //fill text view
                        heart.setText("Chance of heart disease: 1");
                    }
                    else {
                        heart.setText("Chance of heart disease: 0");

                    }
                    if(response.get("diabetes").equals("0") & response.get("cancer").equals("0") & response.get("heart_disease").equals("0")){
                        Toast.makeText(Tabs.this,"No results to return.", Toast.LENGTH_SHORT).show();
                    }


                } catch (JSONException e) {
                    e.printStackTrace();
                }
                System.out.println(response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                if(listener!=null){
                    error.getCause();
                }
            }
        });

        requestQueue.add(stringRequest);
    }

    public void submitReview(View view) throws JSONException {
        JSONObject reviewObject = new JSONObject();
        final TextView review = findViewById(R.id.review);


        final String url = "http://mp00152561.pythonanywhere.com/review";
        final RequestQueue requestQueue = Volley.newRequestQueue(Tabs.this);
        reviewObject.put("user_email", email);
        reviewObject.put("review",review.getText().toString());

        final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url, reviewObject, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {
                try {
                   if(response.get("received").equals("Review Received")){
                       Toast.makeText(Tabs.this,"Review sent", Toast.LENGTH_SHORT).show();
                       review.setText("");

                   }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                System.out.println(response);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                if (listener != null) {
                    error.getCause();
                }
            }
        });

        requestQueue.add(stringRequest);
    }
}