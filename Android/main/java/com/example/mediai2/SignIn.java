package com.example.mediai2;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoDatabase;

import org.json.JSONException;
import org.json.JSONObject;


public class SignIn extends AppCompatActivity {
    public String usernameString;
    private Response.Listener listener;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void signIn(View view) throws JSONException {
        final EditText username =  findViewById(R.id.username);
        EditText password =  findViewById(R.id.password);


        if(username.getText().toString().isEmpty()  || password.getText().toString().isEmpty()){
            //display message to user that the name isn't valid
            Log.i("username/password empty", "must not be empty");
            Toast.makeText(SignIn.this,"Invalid username or password.", Toast.LENGTH_SHORT).show();

        }
        if(username.getText().toString().contains("@") ){
            // shows message to the logcat that the name is valid
            Log.i("Username: ", username.getText().toString());
            Log.i("Password: ", password.getText().toString());
            usernameString = username.getText().toString();

            JSONObject loginInfo = new JSONObject();
            loginInfo.put("email",usernameString);
            loginInfo.put("password", password.getText().toString());


            final String url = "http://mp00152561.pythonanywhere.com/phone_login";
            RequestQueue requestQueue = Volley.newRequestQueue(SignIn.this);

            final JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url,loginInfo, new Response.Listener<JSONObject>() {

                @Override
                public void onResponse(JSONObject response) {
                    try {
                        response.get("login");
                        if(response.get("login").equals("success")){
                            System.out.println("success");
                            Toast.makeText(SignIn.this,"Welcome " + usernameString, Toast.LENGTH_SHORT).show();
                            Intent intent = new Intent(getApplicationContext(), Tabs.class);
                            intent.putExtra("username", usernameString);
                            startActivity(intent);
                        }
                        else {
                            System.out.println("2");
                            Toast.makeText(SignIn.this,"It is unlikely that you have breast cancer.", Toast.LENGTH_SHORT).show();
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

            //opens up the tabbed activity page.


        }
        else{
            Log.i("Ussername: ", username.getText().toString());
            Toast.makeText(SignIn.this,"Invalid. Please Try Again.", Toast.LENGTH_SHORT).show();

        }


    }
    public void register(View view){
        Log.i("Hello"," world.");
        Toast.makeText(SignIn.this,"Hello",Toast.LENGTH_SHORT).show();
        Intent intent = new Intent(getApplicationContext(), Register.class);
        startActivity(intent);
    }
}
