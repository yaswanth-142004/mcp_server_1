from fastmcp import FastMCP 


mcp = FastMCP("Personal Server")

@mcp.tool
def get_my_details(secret_code:str):
    
    info = {
        "name":"yaswanth",
        "age":20,
        "work":"SDE-AI",
        "about":"Can build sophisticated agents along with a amazing web applications",
        "hobbies":"can cook your soul soothing food , can code for 20 hrs a day and can listen to all your bullshit."
        
        
    }
    
    return info
    
    
    
    
if __name__ == "__main__":
    mcp.run(transport="http",port=1234)
    
    
    