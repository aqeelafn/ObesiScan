import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import pickle

with open('logistic_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

def preprocess_input(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess input data"""
    # Replace categorical values with numerical values
    data.replace({
        'yes': 1, 'no': 0,
        'female': 0, 'male': 1,
        'never': 2, 'sometimes': 3, 'always': 4,
        '1': 0, '2': 1, '3': 2, '4': 3,
        'frequently': 5,
        'between 1 and 2 l': 0, 'less than a liter': 1, 'more than 2 l': 2,
        '0': 0, '1 to 2': 1, '2 to 4': 2, '4 to 5': 3,
        '0 to 2': 0, '3 to 5': 1, '>5': 2,
        'walking': 0, 'bike': 1, 'motorbike': 2, 'automobile': 3, 'public_transportation': 4
    }, inplace=True)
    return data

with st.sidebar:
    selected = option_menu("Menu", ["Home", 'Predict'],
                           icons=['house', 'activity'], menu_icon="cast", default_index=0)

if selected == 'Home':
    st.title('Selamat Datang di ObesiScan')
    st.image("https://images.thequint.com/thequint-fit%2F2019-12%2F1fc97a27-15ca-470e-a12a-ceaecb2207f9%2FiStock_1136537470.jpg?auto=format%2Ccompress&fmt=webp&width=720&w=1200", width=500)
    st.write("Selamat datang di ObesiScan!")
    st.write("Temukan rahasia sehat dan kebahagiaan dengan memprediksi risiko obesitas Anda berdasarkan gaya hidup dan faktor kesehatan Anda.")

    with st.expander("Kenapa Kita Harus Sadar akan Obesitas?"):
        st.markdown("### **Mengapa Harus Peduli tentang Obesitas?**")
        st.image("https://www.publichealthnotes.com/wp-content/uploads/2023/04/obesity-title-image.jpg", width=500)
        st.write("""
        Obesitas adalah kondisi medis yang kompleks dan sering kali diabaikan. Namun, menyadari pentingnya obesitas sangatlah penting karena dapat membawa konsekuensi serius terhadap kesehatan. Berikut adalah beberapa alasan mengapa kita harus peduli tentang obesitas:

        1. **Risiko Penyakit Serius**: Obesitas dapat meningkatkan risiko Anda terkena penyakit jantung, diabetes tipe 2, kanker, dan berbagai penyakit lainnya.

        2. **Kualitas Hidup yang Buruk**: Obesitas dapat mengganggu aktivitas sehari-hari Anda dan membatasi mobilitas Anda, mempengaruhi kualitas hidup secara keseluruhan.

        3. **Kesehatan Mental**: Selain dampak fisiknya, obesitas juga dapat memengaruhi kesehatan mental Anda, meningkatkan risiko depresi dan kecemasan.

        4. **Biaya Perawatan Kesehatan**: Mengobati kondisi medis yang berkaitan dengan obesitas dapat menjadi mahal, menimbulkan beban finansial bagi individu dan sistem perawatan kesehatan secara keseluruhan.

        5. **Pencegahan Lebih Baik daripada Pengobatan**: Mengetahui dan mencegah obesitas lebih baik daripada mengobatinya setelah terjadi. Kesadaran dan tindakan preventif dapat membantu mencegah masalah kesehatan yang berkaitan dengan obesitas.

        Memahami betapa pentingnya kesadaran akan obesitas adalah langkah pertama menuju hidup yang lebih sehat dan bahagia.
        """)
    with st.expander("Bagaimana Cara Kerjanya?"):
        st.markdown("### **Bagaimana Aplikasi Ini Bekerja?**")
        st.image("https://png.pngtree.com/png-clipart/20220302/ourlarge/pngtree-smart-men-thinking-or-solving-problem-illustration-png-image_4471284.png", width=300)
        st.write("""
        Aplikasi ini bekerja dengan memanfaatkan data kesehatan yang Anda masukkan di halaman **Predict**. Data ini kemudian diproses menggunakan algoritma canggih untuk menganalisis risiko obesitas Anda. Hasil analisis akan ditampilkan kepada Anda dalam bentuk prediksi yang akurat, memungkinkan Anda untuk memahami dan mengelola risiko obesitas dengan lebih baik.

        **Langkah-langkah Cara Kerjanya:**
        1. **Masukkan Data Kesehatan**: Isi formulir dengan data kesehatan Anda di halaman **Predict**.
        2. **Analisis Data**: Data Anda akan diproses menggunakan algoritma untuk menganalisis risiko obesitas.
        3. **Tampilkan Hasil**: Hasil prediksi akan ditampilkan kepada Anda dalam bentuk yang mudah dimengerti.
        """)
    with st.expander("Manfaat Aplikasi"):
        st.markdown("### **Manfaat Menggunakan Aplikasi Ini**")
        st.image("https://image.freepik.com/free-vector/health-benefits-concept_23-2148172633.jpg", width=350)
        st.write("""

        **1. Kesadaran Kesehatan**: Dengan menggunakan aplikasi ini, Anda akan lebih sadar akan faktor risiko obesitas dan dampaknya terhadap kesehatan Anda.

        **2. Prediksi Obesitas**: Aplikasi ini menggunakan algoritma canggih untuk memberikan prediksi obesitas, membantu Anda untuk mengambil langkah-langkah preventif yang tepat.

        **3. Informasi yang Mudah Dipahami**: Hasil analisis akan ditampilkan dalam bentuk yang mudah dimengerti, sehingga Anda dapat dengan cepat dan efektif memahami tingkat risiko obesitas Anda.

        **4. Langkah-langkah Preventif**: Berdasarkan prediksi, Anda dapat mengambil langkah-langkah preventif yang sesuai untuk menjaga kesehatan Anda dan mencegah masalah kesehatan yang berkaitan dengan obesitas.
        """)

if selected == 'Predict':
    st.title('ObsiScan')
    #st.write('Obesitas telah menjadi masalah kesehatan global yang serius. Deteksi dini sangatlah penting untuk mencegah komplikasi berbahaya. Oleh karena itu, aplikasi ini dikembangkan untuk melakukan prediksi obesitas berdasarkan faktor pola hidup sehari-hari.')
    #st.write("")
    
    with st.form("my_form"):
        gender = st.selectbox('Gender', ['male', 'female'])
        age = st.number_input('Age', min_value=1, max_value=150, step=1)
        height = st.number_input('Height (in meters)', min_value=0.01, max_value=3.0, step=0.01)
        weight = st.number_input('Weight (in Kilograms)', min_value=1, max_value=500, step=1)
        # Family history with overweight
        family_history = st.radio('Family history with overweight', ['yes', 'no'])
        # FAVC (Frequency of consumption of high caloric food)
        favc = st.radio('Frequency of consumption of high caloric food (FAVC)', ['yes', 'no'])
        # FCVC (Frequency of consumption of vegetables)
        fcvc = st.selectbox('Frequency of consumption of vegetables (FCVC)', ['always', 'never', 'sometimes'])
        # NCP (Number of main meals)
        ncp = st.number_input('Number of main meals (NCP)', min_value=0, step=1)
        # CAEC (Consumption of food between meals)
        caec = st.selectbox('Consumption of food between meals (CAEC)', ['no', 'sometimes', 'frequently', 'always'])
        # SMOKE
        smoke = st.radio('Smoking habit', ['yes', 'no'])
        # CH2O (Consumption of water daily)
        ch2o = st.selectbox('Consumption of water daily (CH2O)', ['between 1 and 2 l', 'more than 2 l', 'less than a liter'])
        # SCC (Calories consumption monitoring)
        scc = st.radio('Calories consumption monitoring (SCC)', ['yes', 'no'])
        # FAF (Physical activity frequency)
        faf = st.selectbox('Physical activity frequency (FAF)', ['0', '4 to 5', '2 to 4', '1 to 2'])
        # TUE (Time using technology devices)
        tue = st.selectbox('Time using technology devices (TUE)', ['3 to 5', '0 to 2', '>5'])
        # CALC (Consumption of alcohol)
        calc = st.selectbox('Consumption of alcohol (CALC)', ['no', 'sometimes', 'frequently', 'always'])
        # MTRANS (Transportation used)
        mtrans = st.selectbox('Transportation used (MTRANS)', ['public_transportation', 'walking', 'automobile', 'motorbike', 'bike'])
        # bmi = st.number_input('Number of Body Mass Index (BMI)', min_value=0.0, max_value=100.0, step=0.1)
        
        button_submit = st.form_submit_button("Submit")

    if height == 0:
        height = 0.1
    bmi = weight/(height**2)

    if age != 0.0:
        if age < 1.0:
            st.warning(f"Peringatan: Umur yang Anda masukkan ({age}) mungkin terlalu rendah. Harap periksa kembali masukan Anda.")
    if height != 0.0:
        if height <= 0.5:
            st.warning(f"Peringatan: Nilai tinggi badan yang Anda masukkan ({height}) mungkin terlalu rendah. Harap periksa kembali masukan Anda.")
    if weight != 0.0:
        if weight <= 2.0:
            st.warning(f"Peringatan: Nilai berat badan yang Anda masukkan ({weight}) mungkin terlalu rendah. Harap periksa kembali masukan Anda.")

    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'family_history_with_overweight': [family_history],
        'FAVC': [favc],
        'FCVC': [fcvc],
        'NCP': [ncp],
        'CAEC': [caec],
        'SMOKE': [smoke],
        'CH2O': [ch2o],
        'SCC': [scc],
        'FAF': [faf],
        'TUE': [tue],
        'CALC': [calc],
        'MTRANS': [mtrans],
        'BMI': [bmi]
    })

    if button_submit:
        if age == 0 or height == 0 or weight == 0 or ncp == 0:
            st.error('Harap melengkapi data di atas')
        else:
            processed_input = preprocess_input(input_data)
            label = loaded_model.predict(processed_input)[0]
            col_1, col_2 = st.columns([1,4])
            if label == "insufficient_weight":
                # st.subheader("Insufficient Weight")
                if gender == "male":
                    col_1.image("gambar/i cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/i cewe.png", width=100)
                with col_2:
                    st.write("### Berat Kurang: BMI di bawah 18.5")
                    st.info("Anda sebaiknya mempertimbangkan untuk meningkatkan asupan kalori Anda dan/atau berkonsultasi dengan profesional kesehatan.")
                    st.write("Cobalah untuk menambah porsi makan atau memilih makanan yang lebih kaya kalori. **Pastikan Anda tetap mengonsumsi makanan yang sehat!**")

            elif label == "normal_weight":
                # st.subheader("Normal Weight")
                if gender == "male":
                    col_1.image("gambar/normal cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/normal cwe.png", width=100)
                with col_2:
                    st.write("### Berat Normal: BMI 18.5 - 24.9")
                    st.success("Selamat! Berat badan Anda berada dalam rentang yang sehat.")
                    st.write("Lanjutkan pola makan seimbang dan aktivitas fisik rutin untuk mempertahankan berat badan ideal Anda. **Teruskan gaya hidup sehat Anda!**")

            elif label == "overweight_level_i":
                # st.subheader("Overweight Level 1")
                if gender == "male":
                    col_1.image("gambar/overweight cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/overweight cwe.png", width=100)
                with col_2:
                    st.write("### Overweight Level I: BMI 25.0 - 29.9")
                    st.warning("Anda mungkin perlu mempertimbangkan untuk melakukan perubahan pada pola makan dan rutinitas olahraga Anda.")
                    st.write("Mulailah dengan perubahan kecil seperti mengurangi asupan gula dan lemak jenuh, serta meningkatkan aktivitas fisik harian Anda.")

            elif label == "overweight_level_ii":
                # st.subheader("Overweight Level 2")
                if gender == "male":
                    col_1.image("gambar/overweight cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/overweight cwe.png", width=100)
                with col_2:
                    st.write("### Overweight Level II: BMI 30.0 - 34.9")
                    st.warning("Penting untuk fokus pada pengadopsian gaya hidup yang lebih sehat untuk mengurangi risiko kesehatan.")
                    st.write("Pertimbangkan untuk berkonsultasi dengan ahli gizi untuk mendapatkan rencana diet yang sesuai serta tingkatkan intensitas olahraga secara bertahap.")

            elif label == "obesity_type_i":
                # st.subheader("Obesity Type 1")
                if gender == "male":
                    col_1.image("gambar/obesity 1 2 cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/obesity 1 2 cwe.png", width=100)
                with col_2:
                    st.write("### Obesitas Tipe I: BMI 35.0 - 39.9")
                    st.error("Sangat penting untuk mengatasi obesitas guna mencegah komplikasi kesehatan terkait.")
                    st.write("Buatlah rencana penurunan berat badan yang terstruktur dengan bantuan profesional kesehatan. **Setiap langkah kecil menuju gaya hidup sehat sangat berarti!**")

            elif label == "obesity_type_ii":
                # st.subheader("Obesity Type 2")
                if gender == "male":
                    col_1.image("gambar/obesity 1 2 cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/obesity 1 2 cwe.png", width=100)
                with col_2:
                    st.write("### Obesitas Tipe II: BMI 40.0 - 49.9")
                    st.error("Tindakan segera diperlukan untuk mengatasi obesitas berat dan risiko kesehatan terkait.")
                    st.write("Segera konsultasikan dengan dokter untuk penanganan lebih lanjut. **Pendekatan yang tepat dapat membantu Anda mengurangi risiko kesehatan yang serius.**")

            elif label == "obesity_type_iii":
                # st.subheader("Obesity_Type 3")
                if gender == "male":
                    col_1.image("gambar/obesity 3 cowo.png", width=100)  # Ganti URL dengan gambar yang sesuai
                else:
                    col_1.image("gambar/obesity 3 cwe.png", width=100)
                with col_2:
                    st.write("### Obesitas Tipe III: BMI di atas 50.0")
                    st.error("Obesitas ekstrem memerlukan perhatian segera dan manajemen medis komprehensif.")
                    st.write("Penanganan intensif dan dukungan medis diperlukan. **Jangan ragu untuk mencari bantuan profesional untuk perawatan yang tepat.**")