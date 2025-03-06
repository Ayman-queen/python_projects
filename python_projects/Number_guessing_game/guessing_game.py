import streamlit as st
import random

# Streamlit UI setup
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

st.title("🎯 Number Guessing Game!")
st.write("Guess a number between **50 and 100**. Can you win?")

# Choose difficulty level
difficulty = st.selectbox("Select Difficulty:", ["Easy (7 attempts)", "Medium (5 attempts)", "Hard (3 attempts)"])

# Set attempts based on difficulty
if difficulty == "Easy (7 attempts)":
    max_attempts = 7
elif difficulty == "Medium (5 attempts)":
    max_attempts = 5
else:
    max_attempts = 3

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.attempts_taken = 0
    st.session_state.score = 100
    st.session_state.game_over = False

# Display remaining attempts
st.write(f"**Attempts Remaining:** {max_attempts - st.session_state.attempts_taken}")

# Get user input
user_guess = st.number_input("Enter your guess:", min_value=50, max_value=100, step=1)

# "Guess" button
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
                # Provide hints
                difference = abs(user_guess - st.session_state.number_to_guess)
                if difference >= 20:
                    hint = "❄️ Ice cold!"
                elif difference >= 10:
                    hint = "🥶 Cold!"
                elif difference >= 5:
                    hint = "🔥 Getting warm!"
                else:
                    hint = "🔥🔥 Hot! Almost there!"

                if user_guess > st.session_state.number_to_guess:
                    st.warning(f"📉 Too high! {hint} Try again.")
                else:
                    st.warning(f"📈 Too low! {hint} Try again.")

# Restart button
if st.button("Restart Game"):
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.attempts_taken = 0
    st.session_state.score = 100
    st.session_state.game_over = False
    st.experimental_rerun()

        else:
            print(YELLOW + f"📈 Too low! {hint} Try again." + RESET)

# Game Over Message
print("\n" + CYAN + "🎮 Thanks for playing! Want to try again? Run the game again!" + RESET)
