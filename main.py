import traceback

# 1. The Application Code containing a mathematical bug
def perform_calculation(data_input):
    print(f"[App] Running calculation with input: {data_input}")
    # BUG: If data_input is 0, this will cause a ZeroDivisionError crash
    return 100 / data_input

# 2. Automated Program Repair / Self-Healing Simulation
def automated_repair_handler(failed_input, error_message):
    print(f"\n[Healer] Analyzing crash log...")
    print(f"[Healer] Error detected: {error_message}")
    
    print("[Healer] Synthesizing program repair...")
    # Simulating a logic correction patch
    if "division by zero" in str(error_message).lower():
        print("[Healer] Patch found: Redirecting zero input to a safe default boundary.")
        fallback_input = 0.000001
        
        # Retry the logic with the patch applied
        patched_result = perform_calculation(fallback_input)
        return patched_result
    else:
        print("[Healer] Unknown error. Cannot synthesize patch.")
        raise

# 3. The Execution Loop
if __name__ == "__main__":
    test_input = 0  # This input triggers the bug
    
    try:
        # Attempt to run the bad code
        result = perform_calculation(test_input)
        print(f"[Success] Calculation completed: {result}")
    except Exception as e:
        print("[System] Software crashed! Redirecting to automated repair infrastructure...")
        # Pass the failure variables to the repair handler to resolve the crash safely
        final_result = automated_repair_handler(test_input, e)
        print(f"\n[Success] System stabilized via automation. Fixed Output: {final_result}")
      
