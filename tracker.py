import streamlit as st
import random
import time


def step_tracker(goal_steps):

    st.subheader("🚶 Walking Progress Tracker")

    if goal_steps is None:
        st.warning("Generate recommendation first.")
        return

    if "current_steps" not in st.session_state:
        st.session_state.current_steps = 0

    if "tracking" not in st.session_state:
        st.session_state.tracking = False

    if "paused" not in st.session_state:
        st.session_state.paused = False

    if "goal_completed" not in st.session_state:
        st.session_state.goal_completed = False

    if "streak" not in st.session_state:
        st.session_state.streak = 0
    
    if "start_time" not in st.session_state:
        st.session_state.start_time = None
    
    
    mode = st.selectbox("🚶 Walking Speed", ["Slow", "Normal", "Fast"])

    if mode == "Slow":
        steps_per_sec = 1
    elif mode == "Normal":
        steps_per_sec = 2
    else:
        steps_per_sec = 3

    col1, col2, col3 = st.columns(3)

    if col1.button("▶ Start"):
        st.session_state.tracking = True
        st.session_state.paused = False
        st.session_state.goal_completed = False
        if st.session_state.start_time is None:
            st.session_state.start_time = time.time()

    if col2.button("⏸ Pause"):
        st.session_state.paused = True

    if col3.button("🔄 Reset"):
        st.session_state.current_steps = 0
        st.session_state.tracking = False
        st.session_state.paused = False
        st.session_state.goal_completed = False
        st.session_state.start_time = None

    steps = st.session_state.current_steps
    progress = min(steps / goal_steps, 1.0)

    st.progress(progress)
    st.write(f"👣 Steps: {steps} / {goal_steps}")

    if st.session_state.start_time:
        elapsed_time = (time.time() - st.session_state.start_time) / 60
    else:
        elapsed_time = 0
    calories = steps * 0.04
    st.write(f"Calories Burned: {calories:.1f} kcal")

    remaining = goal_steps - steps
    st.write(f"Remaining Steps: {max(remaining,0)}steps")

    distance = steps * 0.0008
    st.write(f"📍 Distance: {distance:.2f} km")

    st.write(f"⏱ Time: {elapsed_time:.1f} min")

    st.subheader("🏆 Achievement")

    if steps >= goal_steps:
        st.success("🎉 Goal Completed!")
    elif steps >= goal_steps * 0.7:
        st.info("👍 Almost there!")
    else:
        st.warning("🚶 Keep going!")

    if steps >= goal_steps and not st.session_state.goal_completed:
        st.session_state.streak += 1
        st.session_state.goal_completed = True

    st.write(f"🔥 Streak: {st.session_state.streak} days")

    if st.session_state.tracking and not st.session_state.paused:

        time.sleep(1)

        st.session_state.current_steps += random.randint(3, 4)

        if st.session_state.current_steps >= goal_steps:
            st.session_state.current_steps = goal_steps
            st.session_state.tracking = False
            st.session_state.goal_completed = True


        st.rerun()