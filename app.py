import streamlit as st
import numpy as np
import joblib

modelo = joblib.load("modelo_logistic.pkl")
