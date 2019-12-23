package com.example.mediai2;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class Register extends AppCompatActivity {
    private RequestQueue requestQueue;
    private Response.Listener listener;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
    }

    public void sendToDataBase(View view) throws Exception{
        final EditText firstName = findViewById(R.id.registerFirstNameField);
        EditText secondName = findViewById(R.id.registerSecondNameField);
        EditText email = findViewById(R.id.registerEmailField);
        EditText pass = findViewById(R.id.registerPasswordField);
        EditText passRe = findViewById(R.id.registerReenterField);
        EditText doctor = findViewById(R.id.registerDoctorsNameField);

        String fNameString  = firstName.getText().toString();
        String sNameString = secondName.getText().toString();
        final String emailString = email.getText().toString();
        String passString = pass.getText().toString();
        String passReString = passRe.getText().toString();
        String docReString = doctor.getText().toString();


        if (fNameString.isEmpty() || sNameString.isEmpty() || emailString.isEmpty() || passString.isEmpty() || passReString.isEmpty()){
            Toast.makeText(Register.this,"Please fill all the text fields.", Toast.LENGTH_SHORT).show();
        }
        else{
            if(emailString.contains("@")){
                if (passString.equals(passReString)){
                    JSONObject person =  new JSONObject();

                    person.put("first_name", fNameString);
                    person.put("surname", sNameString);
                    person.put("email", emailString);
                    person.put("password",passString);
                    person.put("doctor_name", docReString);




                    //Then send the JSON object to the dataset
                    final String url = "http://mp00152561.pythonanywhere.com/phone_register";
                    RequestQueue requestQueue = Volley.newRequestQueue(Register.this);
                    System.out.println();

                    final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,person, new Response.Listener<JSONObject>() {

                        @Override
                        public void onResponse(JSONObject response) {
                            try {
                                response.get("valid");
                                System.out.println(response.get("valid"));
                                if(response.get("valid").equals("0")){
                                    Toast.makeText(Register.this,"That email already exists. Please try again.", Toast.LENGTH_SHORT).show();
                                }
                                else if(response.get("valid").equals("1")){
                                    Toast.makeText(Register.this,"That doctor doesn't exist. Please try again.", Toast.LENGTH_SHORT).show();
                                }
                                else {
                                    Toast.makeText(Register.this,"Welcome" + emailString, Toast.LENGTH_SHORT).show();
                                    Intent intent = new Intent(getApplicationContext(), Tabs.class);
                                    intent.putExtra("username", emailString);
                                    startActivity(intent);
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
                else {
                    Toast.makeText(Register.this,"Passwords don't match", Toast.LENGTH_SHORT).show();
                }
                }
                else {
                Toast.makeText(Register.this,"That email is not valid", Toast.LENGTH_SHORT).show();
                }
            }
        }
}
