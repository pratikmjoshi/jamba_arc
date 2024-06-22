import streamlit as st
from constants import DEFAULT_MODEL
from constants import client
from ai21.models import Penalty


def generate(prompt, max_tokens=240):

    res = client.completion.create(
        model=DEFAULT_MODEL,
        prompt=prompt,
        num_results=1,
        max_tokens=max_tokens,
        temperature=1,
        top_k_return=0,
        top_p=0.98,
        count_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        frequency_penalty=Penalty(
            scale=225,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        presence_penalty=Penalty(
            scale=1.2,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        )
    )

    return res.completions[0].data.text


def count_tokens(text):
    return client.count_tokens(text=text)