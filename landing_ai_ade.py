import os
import toml
from pathlib import Path
from landingai_ade import LandingAIADE

toml_set = toml.load('secrets.toml')
os.environ['VISION_AGENT_API_KEY'] = toml_set['VISION_AGENT_API_KEY']

#Initialize client
client = LandingAIADE(
    apikey=os.environ.get("VISION_AGENT_API_KEY")
)


if __name__ == "__main__":
    #Process files within 'Test' repo of larger project folder
    directory_to_process = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Test")
    if os.path.exists(directory_to_process):
        print(f"Processing files in: {directory_to_process}")
        for root, _, files in os.walk(directory_to_process):
            # Skip RESOURCE.FRK folder
            if "RESOURCE.FRK" in root:
                continue
                
            for file in files:
                file_path = os.path.join(root, file)
                
                try:
                    response = client.parse(document=Path(file_path), model="dpt-2-mini")

                    if response.markdown:
                        print(f"Successfully processed {file_path}")
                        markdown = response.markdown
                        # Save the markdown to a .md file
                        output_file = Path(file_path).with_suffix('.md')
                        with open(output_file, 'w', encoding='utf-8') as md_file:
                            md_file.write(markdown)
                    else:
                        print(f"Failed to process {file_path}: {response.text}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

    else:
        print(f"Directory not found: {directory_to_process}")