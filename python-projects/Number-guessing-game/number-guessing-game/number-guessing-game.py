import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")
st.title("🎯 Number Guessing Game!")
st.write("Guess a number between **50 and 100**. Can you win?")
difficulty = st.selectbox("Select Difficulty:", ["Easy (7 attempts)", "Medium (5 attempts)", "Hard (3 attempts)"])
max_attempts = 7 if difficulty == "Easy (7 attempts)" else 5 if difficulty == "Medium (5 attempts)" else 3

if "number_to_guess" not in st.session_state:
  st.session_state.number_to_guess = random.randint(50, 100)
  st.session_state.attempts_taken = 0
  st.session_state.score = 100
  st.session_state.game_over = False

st.write(f"**Attempts Remaining:** {max_attempts - st.session_state.attempts_taken}")
user_guess = st.number_input("Enter your guess:", min_value=50, max_value=100, step=1)

if st.button("Guess"):
  if st.session_state.game_over:
    st.warning("Game over! Refresh to play again.")
  else:
    st.session_state.attempts_taken += 1
    if user_guess == st.session_state.number_to_guess:
      st.success(f"🎉 Correct! You guessed {user_guess} in {st.session_state.attempts_taken} attempts!")
      st.write(f"🏆 Your Score: {st.session_state.score} points")
      st.session_state.game_over = True
    else:
      st.session_state.score -= 10
      if st.session_state.attempts_taken == max_attempts:
        st.error(f"❌ Game Over! The correct number was {st.session_state.number_to_guess}.")
        st.write(f"🏆 Final Score: {st.session_state.score} points")
        st.session_state.game_over = True
      else:
        difference = abs(user_guess - st.session_state.number_to_guess)
        hint = "❄️ Ice cold!" if difference >= 20 else "🥶 Cold!" if difference >= 10 else "🔥 Getting warm!" if difference >= 5 else "🔥🔥 Hot! Almost there!"
        st.warning(f"📉 Too high! {hint} Try again." if user_guess > st.session_state.number_to_guess else f"📈 Too low! {hint} Try again.")

if st.button("Restart Game"):
  st.session_state.number_to_guess = random.randint(50, 100)
  st.session_state.attempts_taken = 0
  st.session_state.score = 100
  st.session_state.game_over = False
  st.rerun()

