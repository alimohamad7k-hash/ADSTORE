import streamlit as st
import urllib.parse

st.set_page_config(page_title="متجري الإلكتروني", page_icon="🛍️", layout="centered")

products = [
    {
        "id": 1,
        "name": "حذاء رياضي أنيق",
        "price": 150,
        "image": "https://via.placeholder.com/300x150.png?text=Sneakers",
        "description": "مريح جداً وعالي الجودة للاستخدام اليومي."
    },
    {
        "id": 2,
        "name": "ساعة يد ذكية",
        "price": 250,
        "image": "https://via.placeholder.com/300x150.png?text=Smartwatch",
        "description": "تتبع اللياقة البدنية والاتصالات بكل سهولة."
    },
    {
        "id": 3,
        "name": "سماعات بلوتوث",
        "price": 120,
        "image": "https://via.placeholder.com/300x150.png?text=Headphones",
        "description": "صوت نقي وبطارية تدوم طويلاً."
    }
]

if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None

if st.session_state.selected_product is None:
    st.title("🛍️ مرحبا بك في متجري")
    st.write("اختر المنتج الذي يناسبك واضغط على 'شري دابا':")
    st.markdown("---")

    for prod in products:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(prod["image"], use_container_width=True)
        with col2:
            st.subheader(prod["name"])
            st.write(prod["description"])
            st.markdown(f"**الثمن:** `{prod['price']} درهم`")
            
            if st.button(f"🛒 شري دابا ({prod['name']})", key=f"btn_{prod['id']}"):
                st.session_state.selected_product = prod
                st.rerun()
        st.markdown("---")

else:
    prod = st.session_state.selected_product
    
    if st.button("⬅️ رجوع إلى قائمة المنتجات"):
        st.session_state.selected_product = None
        st.rerun()

    st.title("📋 إتمام طلب الشراء")
    st.markdown(f"### المنتج المختار: {prod['name']}")
    st.markdown(f"**الثمن الإجمالي:** <span style='color:green; font-size:20px;'>{prod['price']} درهم</span>", unsafe_allow_html=True)
    st.markdown("---")

    with st.form(key="checkout_form"):
        st.subheader("أدخل معلومات التوصيل:")
        full_name = st.text_input("الاسم الكامل:")
        phone = st.text_input("رقم الهاتف (مثال: 06XXXXXXXX):")
        address = st.text_input("المدينة / العنوان:")
        
        submit_order = st.form_submit_button(label="تأكيد الطلب وإرساله عبر الواتساب")

    if submit_order:
        if not full_name or not phone or not address:
            st.error("⚠️ عافاك عمر جميع المعلومات باش تكمل الطلب!")
        else:
            phone_number = "212609962846"
            
            message = (
                f"السلام عليكم، بغيت نطلب هاد المنتج:\n\n"
                f"📦 المنتج: {prod['name']}\n"
                f"💰 الثمن: {prod['price']} درهم\n"
                f"--------------------\n"
                f"👤 الاسم: {full_name}\n"
                f"📞 الهاتف: {phone}\n"
                f"📍 العنوان: {address}"
            )
            
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
            
            st.success("🎉 تم تسجيل طلبك بنجاح! جاري تحويلك إلى الواتساب...")
            st.markdown(f'<meta http-equiv="refresh" content="1;url={whatsapp_url}">', unsafe_allow_html=True)
            st.markdown(f"👉 [اضغط هنا إذا لم يتم تحويلك تلقائياً للواتساب]({whatsapp_url})", unsafe_allow_html=True)
