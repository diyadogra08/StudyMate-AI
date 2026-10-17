import streamlit as st
import ollama


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 StudyMate AI")
with st.sidebar:
    st.title("📚 StudyMate AI")
    st.write("Your Personal AI Study Assistant")
    st.divider()

    page = st.selectbox(
        "Choose a feature",
        [
            "🏠 Home",
            "📖 Topic Explainer",
            "📝 Quiz Generator",
            "📄 Notes Summarizer",
            "🗂️ Flashcard Generator",
            "📅 Study Planner"
        ]
    )
st.subheader("Your Personal AI Study Assistant")
st.info(
    "👋 Welcome to StudyMate AI! "
    "Learn smarter with AI-powered explanations, "
    "quizzes, summaries, flashcards, and study plans."
)

st.write(
    "Welcome! Learn topics, summarize notes, "
    "and prepare for exams with AI."
)

topic = st.text_input("Enter a topic you want to learn")

if st.button("Explain Topic"):
    if topic:
        with st.spinner("AI is preparing your explanation..."):
            try:
                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Explain {topic} in simple language "
                                "for a college student. Give a definition, "
                                "key points, and one example."
                            )
                        }
                    ]
                )

                st.subheader("AI Explanation")
                st.write(response["message"]["content"])

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first.")
        #QUIZ
        st.divider()
st.header("📝 Quiz Generator")

quiz_topic = st.text_input("Enter a topic for your quiz")

if st.button("Generate Quiz"):
    if quiz_topic:
        with st.spinner("Generating quiz..."):
            try:
                quiz_response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Create 5 multiple-choice quiz questions "
                                f"about {quiz_topic} for a college student. "
                                "Give 4 options per question and clearly "
                                "mark the correct answer."
                            )
                        }
                    ]
                )

                st.subheader("Your Quiz")
                st.write(quiz_response["message"]["content"])

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first.")
        #NOTES
        st.divider()
st.header("📄 AI Notes Summarizer")

notes = st.text_area(
    "Paste your study notes here",
    height=200,
    placeholder="Paste your class notes here..."
)

if st.button("Summarize Notes"):
    if notes.strip():
        with st.spinner("Summarizing your notes..."):
            try:
                summary_response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                "Summarize these college study notes "
                                "in simple language. Use headings, "
                                "important points, and key definitions. "
                                "Keep the summary useful for exam revision.\n\n"
                                + notes
                            )
                        }
                    ]
                )

                st.subheader("📝 Your Summary")
                st.write(summary_response["message"]["content"])

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste your notes first.")
        #FLASHCARDS
        st.divider()
st.header("🗂️ AI Flashcard Generator")

flashcard_topic = st.text_input(
    "Enter a topic for flashcards"
)

if st.button("Generate Flashcards"):
    if flashcard_topic.strip():
        with st.spinner("Creating flashcards..."):
            try:
                flashcard_response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Create 5 study flashcards about "
                                f"{flashcard_topic}. For each card, "
                                "write a short Question and its Answer. "
                                "Keep them accurate and easy to revise."
                            )
                        }
                    ]
                )

                st.subheader("📚 Your Flashcards")
                st.write(
                    flashcard_response["message"]["content"]
                )

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first.")
        #STUDY PLANNER
        st.divider()
st.header("📅 AI Study Planner")

study_subject = st.text_input(
    "Enter your subject",
    key="planner_subject"
)

study_hours = st.number_input(
    "Hours available per day",
    min_value=1,
    max_value=12,
    value=2
)

study_days = st.number_input(
    "Days available for preparation",
    min_value=1,
    max_value=30,
    value=7
)

if st.button("Create Study Plan"):
    if study_subject.strip():
        with st.spinner("Creating your study plan..."):
            try:
                plan_response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Create a practical study plan for "
                                f"{study_subject}. I have {study_hours} "
                                f"hours per day and {study_days} days. "
                                "Make a day-wise timetable with topics, "
                                "revision, and practice questions. "
                                "Use simple language and a clear format."
                            )
                        }
                    ]
                )

                st.subheader("📖 Your Study Plan")
                st.write(plan_response["message"]["content"])

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter your subject.")
        #footer
        st.divider()
st.caption("📚 StudyMate AI | Built with Python, Streamlit & Ollama")
st.caption("Your personal AI-powered study companion.")