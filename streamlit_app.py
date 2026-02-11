{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-8e661af2fa61>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"🏢 Employee Leave Approval Prediction\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "st.title(\"🏢 Employee Leave Approval Prediction\")\n",
    "\n",
    "# load model + columns\n",
    "model = joblib.load(\"leave_model.pkl\")\n",
    "columns = joblib.load(\"model_columns.pkl\")\n",
    "\n",
    "st.write(\"Provide details:\")\n",
    "\n",
    "inputs = []\n",
    "\n",
    "for col in columns:\n",
    "    value = st.number_input(col, value=0.0)\n",
    "    inputs.append(value)\n",
    "\n",
    "features = np.array(inputs).reshape(1, -1)\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "\n",
    "    prob = model.predict_proba(features)[0][1]\n",
    "\n",
    "    threshold = 0.7\n",
    "    pred = 1 if prob > threshold else 0\n",
    "\n",
    "    st.subheader(f\"Approval Probability: {prob:.2f}\")\n",
    "\n",
    "    if pred == 1:\n",
    "        st.success(\"✅ Likely Approved\")\n",
    "    else:\n",
    "        st.error(\"❌ Likely Rejected\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
