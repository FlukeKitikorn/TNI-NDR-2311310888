import streamlit as st
import json

def load_stock_list(path=".\Datahandle\settrade\stocklist.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
