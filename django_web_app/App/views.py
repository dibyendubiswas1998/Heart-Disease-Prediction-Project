from django.shortcuts import render, HttpResponse
from .forms import PaitentForm
import pickle


# Create your views here.
def Home(request):
    if request.method == 'POST':
        fm = PaitentForm(request.POST)
        if fm.is_valid():
            # fm.save()
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            is_gender = fm.cleaned_data['sex']
            is_chest_pain = fm.cleaned_data['chest_pain']
            trestbps = fm.cleaned_data['blood_pressure']
            chol = fm.cleaned_data['cholestorol']
            fbs = fm.cleaned_data['blood_sugar']
            is_electro_result = fm.cleaned_data['electrocardiographic_resulter']
            thalach = fm.cleaned_data['heart_rate']
            is_angina = fm.cleaned_data['angina']
            oldpeak = fm.cleaned_data['st_depression']
            is_st_segment = fm.cleaned_data['st_segment']
            ca = fm.cleaned_data['vessels']
            is_thallium_test_result = fm.cleaned_data['thallium_test_result']
            

            # Sex
            if is_gender == 'Male':
                sx = 1
            else:
                sx = 0
            

            # Chest Pain
            if is_chest_pain == 'typical angina':
                cp = 1
            elif is_chest_pain == 'atypical angina':
                cp = 2
            elif is_chest_pain == 'non-anginal pain':
                cp = 3
            else:
                cp = 4
            

            # electrocardiographic results
            if is_electro_result == 'Normal':
                restecg = 0
            elif is_electro_result == 'Abnormality':
                restecg = 1
            else:
                restecg = 2


            # angima
            if is_angina == 'No':
                exang = 0
            else:
                exang = 1
            

            # st_segment
            if is_st_segment == 'Upsloping':
                slope = 1
            elif is_st_segment == 'Flat':
                slope = 2
            else:
                slope = 3
            

            # Thallium test
            if is_thallium_test_result == 'Good':
                thal = 1
            else:
                thal = 0

            
            # Evaluate the model
            try:
            #    age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
            #    63,  1,  3,  145,    233, 1,    0,     150,    0,     2.3,   0,   0,  1
                with open("E:\\Dibyendu\Projects\\1. Machine Learning Projects\\Heart Disease Project-1\\Models_save\\logistic.pickle", 'rb') as f:
                    model = pickle.load(f)
                    prediction = model.predict([[age, sx, cp, trestbps, chol, fbs, restecg, thalach,
                                                 exang, oldpeak, slope, ca, thal  ]])
                    print(prediction)
                    
            except Exception as e:
                print(e)


            fm = PaitentForm()
    else:
         fm = PaitentForm()
   
    return render(request, 'home1.html', {'form':fm})
