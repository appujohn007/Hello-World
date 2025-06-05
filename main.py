import streamlit as st
import subprocess
import shlex

st.title("💻 Shell Command Runner")

command = st.text_input("Enter a command to run:", placeholder="e.g. ping google.com")

if st.button("Run"):
    if command.strip() == "":
        st.warning("Please enter a valid command.")
    else:
        st.success(f"Running: `{command}`")
        output_box = st.empty()
        
        try:
            # Split command safely for subprocess
            process = subprocess.Popen(
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            # Stream output line-by-line
            output = ""
            for line in process.stdout:
                output += line
                output_box.code(output, language="bash")

            process.stdout.close()
            process.wait()

        except Exception as e:
            st.error(f"Error: {e}")
