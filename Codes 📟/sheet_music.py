{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "ijGzTHJJUCPY"
   },
   "outputs": [],
   "source": [
    "# Copyright 2025 Google LLC\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     https://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "VEqbX8OhE8y9"
   },
   "source": [
    "# Sheet Music Analysis with Gemini\n",
    "\n",
    "<table align=\"left\">\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg\" alt=\"Google Colaboratory logo\"><br> Run in Colab\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/colab/import/https:%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fuse-cases%2Fdocument-processing%2Fsheet_music.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN\" alt=\"Google Cloud Colab Enterprise logo\"><br> Run in Colab Enterprise\n",
    "    </a>\n",
    "  </td>       \n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.svgrepo.com/download/217753/github.svg\" alt=\"GitHub logo\"><br> View on GitHub\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/gemini/use-cases/document-processing/sheet_music.ipynb\">\n",
    "      <img src=\"https://lh3.googleusercontent.com/UiNooY4LUgW_oTvpsNhPpQzsstV5W8F7rYgxgGBD85cWJoLmrOzhVs_ksK_vgx40SHs7jCqkTkCk=e14-rj-sc0xffffff-h130-w32\" alt=\"Vertex AI logo\"><br> Open in Vertex AI Workbench\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://goo.gle/4jjsLV9\">\n",
    "      <img width=\"32px\" src=\"https://cdn.qwiklabs.com/assets/gcp_cloud-e3a77215f0b8bfa9b3f611c0d2208c7e8708ed31.svg\" alt=\"Google Cloud logo\"><br> Open in  Cloud Skills Boost\n",
    "    </a>\n",
    "  </td>\n",
    "</table>\n",
    "\n",
    "<div style=\"clear: both;\"></div>\n",
    "\n",
    "<b>Share to:</b>\n",
    "\n",
    "<a href=\"https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg\" alt=\"LinkedIn logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://bsky.app/intent/compose?text=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg\" alt=\"Bluesky logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://twitter.com/intent/tweet?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg\" alt=\"X logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://reddit.com/submit?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png\" alt=\"Reddit logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/sheet_music.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg\" alt=\"Facebook logo\">\n",
    "</a>            \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5ad877ea09dd"
   },
   "source": [
    "| Author |\n",
    "| --- |\n",
    "| [Holt Skinner](https://github.com/holtskinner) |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CkHPv2myT2cx"
   },
   "source": [
    "## Overview\n",
    "\n",
    "[Sheet Music](https://en.wikipedia.org/wiki/Sheet_music) is the primary form of music notation used by composers and performers across the world. These pages contain information about the lyrics, pitches, rhythms, composer, text author, composition date, among others.\n",
    "\n",
    "This notebook illustrates using Gemini to extract this metadata from sheet music PDFs.\n",
    "\n",
    "These prompts and documents were demonstrated in the [Google Cloud Next 2024 session \"What's next with Gemini: Driving business impact with multimodal use cases\"](https://www.youtube.com/watch?v=DqH1R9Pk5RI).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "r11Gu7qNgx1p"
   },
   "source": [
    "## Getting Started\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "No17Cw5hgx12"
   },
   "source": [
    "### Install Google Gen AI SDK for Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "tFy3H3aPgx12"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[33m  WARNING: Failed to remove contents in a temporary directory '/opt/conda/lib/python3.10/site-packages/google/~uth'.\n",
      "  You can safely remove it manually.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: Failed to remove contents in a temporary directory '/opt/conda/lib/python3.10/site-packages/google/~auth2'.\n",
      "  You can safely remove it manually.\u001b[0m\u001b[33m\n",
      "\u001b[0mNote: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install --upgrade -q google-genai PyPDF2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DF4l8DTdWgPY"
   },
   "source": [
    "### Set Google Cloud project information and create client\n",
    "\n",
    "To get started using Vertex AI, you must have an existing Google Cloud project and [enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com).\n",
    "\n",
    "Learn more about [setting up a project and a development environment](https://cloud.google.com/vertex-ai/docs/start/cloud-environment)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "Nqwi-5ufWp_B"
   },
   "outputs": [],
   "source": [
    "import os\n",
    "from google import genai\n",
    "\n",
    "PROJECT_ID = \"qwiklabs-gcp-02-70a2b10d496e\"\n",
    "LOCATION = os.environ.get(\"us-east4\", \"global\")\n",
    "client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "jXHfaVS66_01"
   },
   "source": [
    "### Import libraries\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "lslYAvw37JGQ"
   },
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "from IPython.display import Markdown, display\n",
    "import PyPDF2\n",
    "from google.genai.types import (\n",
    "    GenerateContentConfig,\n",
    "    GoogleSearch,\n",
    "    HarmBlockThreshold,\n",
    "    HarmCategory,\n",
    "    Part,\n",
    "    SafetySetting,\n",
    "    Tool,\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FTMywdzUORIA"
   },
   "source": [
    "### Load the Gemini model\n",
    "\n",
    "Gemini is a multimodal model that supports multimodal prompts. You can include text, image(s), PDFs, audio, and video in your prompt requests."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "7b76801cc9e4"
   },
   "outputs": [],
   "source": [
    "MODEL_ID = \"gemini-2.5-flash\"  # @param {type: \"string\"}\n",
    "\n",
    "config = GenerateContentConfig(\n",
    "    temperature=1.0,\n",
    "    max_output_tokens=8192,\n",
    "    safety_settings=[\n",
    "        SafetySetting(\n",
    "            category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,\n",
    "            threshold=HarmBlockThreshold.BLOCK_ONLY_HIGH,\n",
    "        )\n",
    "    ],\n",
    "    system_instruction=\"You are an expert in musicology and music history.\",\n",
    "    tools=[Tool(google_search=GoogleSearch())],\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Wy75sLb-yjNn"
   },
   "source": [
    "## Extract Structured Metadata from Sheet Music PDF\n",
    "\n",
    "For this example, we will be using the popular classical music book [24 Italian Songs and Arias of the 17th and 18th Centuries](https://imslp.org/wiki/24_Italian_Songs_and_Arias_of_the_17th_and_18th_Centuries_(Various)), and extracting metadata about each song in the book."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "0ed417af1e5c"
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[6], line 16\u001b[0m\n\u001b[1;32m      3\u001b[0m sheet_music_extraction_prompt \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\"\"\u001b[39m\u001b[38;5;124mThe following document is a book of sheet music. Your task is to output structured metadata about every piece of music in the document.\u001b[39m\n\u001b[1;32m      4\u001b[0m \n\u001b[1;32m      5\u001b[0m \u001b[38;5;124mCorrect any mistakes that are in the document and fill in missing information when not present in the document.\u001b[39m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[38;5;124mA description of the piece\u001b[39m\n\u001b[1;32m     13\u001b[0m \u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[1;32m     15\u001b[0m \u001b[38;5;66;03m# Send to Gemini\u001b[39;00m\n\u001b[0;32m---> 16\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmodels\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgenerate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m     17\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mMODEL_ID\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     18\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\n\u001b[1;32m     19\u001b[0m \u001b[43m        \u001b[49m\u001b[43msheet_music_extraction_prompt\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     20\u001b[0m \u001b[43m        \u001b[49m\u001b[38;5;66;43;03m# Load file directly from Google Cloud Storage\u001b[39;49;00m\n\u001b[1;32m     21\u001b[0m \u001b[43m        \u001b[49m\u001b[43mPart\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfrom_uri\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m     22\u001b[0m \u001b[43m            \u001b[49m\u001b[43mfile_uri\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43msheet_music_pdf_uri\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     23\u001b[0m \u001b[43m            \u001b[49m\u001b[43mmime_type\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mapplication/pdf\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[1;32m     24\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     25\u001b[0m \u001b[43m    \u001b[49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     26\u001b[0m \u001b[43m    \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mconfig\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     27\u001b[0m \u001b[43m)\u001b[49m\n\u001b[1;32m     29\u001b[0m \u001b[38;5;66;03m# Display results\u001b[39;00m\n\u001b[1;32m     30\u001b[0m display(Markdown(response\u001b[38;5;241m.\u001b[39mtext))\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:5203\u001b[0m, in \u001b[0;36mModels.generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   5201\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m remaining_remote_calls_afc \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[1;32m   5202\u001b[0m   i \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[0;32m-> 5203\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_generate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   5204\u001b[0m \u001b[43m      \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmodel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcontents\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparsed_config\u001b[49m\n\u001b[1;32m   5205\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   5207\u001b[0m   function_map \u001b[38;5;241m=\u001b[39m _extra_utils\u001b[38;5;241m.\u001b[39mget_function_map(parsed_config)\n\u001b[1;32m   5208\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m function_map:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:3985\u001b[0m, in \u001b[0;36mModels._generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   3982\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mconvert_to_dict(request_dict)\n\u001b[1;32m   3983\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mencode_unserializable_types(request_dict)\n\u001b[0;32m-> 3985\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_api_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   3986\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mpost\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpath\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_dict\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\n\u001b[1;32m   3987\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   3989\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m config \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(\n\u001b[1;32m   3990\u001b[0m     config, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mshould_return_http_response\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   3991\u001b[0m ):\n\u001b[1;32m   3992\u001b[0m   return_value \u001b[38;5;241m=\u001b[39m types\u001b[38;5;241m.\u001b[39mGenerateContentResponse(sdk_http_response\u001b[38;5;241m=\u001b[39mresponse)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1388\u001b[0m, in \u001b[0;36mBaseApiClient.request\u001b[0;34m(self, http_method, path, request_dict, http_options)\u001b[0m\n\u001b[1;32m   1378\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mrequest\u001b[39m(\n\u001b[1;32m   1379\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m   1380\u001b[0m     http_method: \u001b[38;5;28mstr\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m   1383\u001b[0m     http_options: Optional[HttpOptionsOrDict] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m   1384\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m SdkHttpResponse:\n\u001b[1;32m   1385\u001b[0m   http_request \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_build_request(\n\u001b[1;32m   1386\u001b[0m       http_method, path, request_dict, http_options\n\u001b[1;32m   1387\u001b[0m   )\n\u001b[0;32m-> 1388\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[1;32m   1389\u001b[0m   response_body \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1390\u001b[0m       response\u001b[38;5;241m.\u001b[39mresponse_stream[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mresponse_stream \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1391\u001b[0m   )\n\u001b[1;32m   1392\u001b[0m   \u001b[38;5;28;01mreturn\u001b[39;00m SdkHttpResponse(headers\u001b[38;5;241m=\u001b[39mresponse\u001b[38;5;241m.\u001b[39mheaders, body\u001b[38;5;241m=\u001b[39mresponse_body)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1224\u001b[0m, in \u001b[0;36mBaseApiClient._request\u001b[0;34m(self, http_request, http_options, stream)\u001b[0m\n\u001b[1;32m   1221\u001b[0m     retry \u001b[38;5;241m=\u001b[39m tenacity\u001b[38;5;241m.\u001b[39mRetrying(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mretry_kwargs)\n\u001b[1;32m   1222\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m retry(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_request_once, http_request, stream)  \u001b[38;5;66;03m# type: ignore[no-any-return]\u001b[39;00m\n\u001b[0;32m-> 1224\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_retry\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request_once\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:477\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    475\u001b[0m retry_state \u001b[38;5;241m=\u001b[39m RetryCallState(retry_object\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m, fn\u001b[38;5;241m=\u001b[39mfn, args\u001b[38;5;241m=\u001b[39margs, kwargs\u001b[38;5;241m=\u001b[39mkwargs)\n\u001b[1;32m    476\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m--> 477\u001b[0m     do \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43miter\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    478\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m         \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:378\u001b[0m, in \u001b[0;36mBaseRetrying.iter\u001b[0;34m(self, retry_state)\u001b[0m\n\u001b[1;32m    376\u001b[0m result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m    377\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m action \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39miter_state\u001b[38;5;241m.\u001b[39mactions:\n\u001b[0;32m--> 378\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43maction\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    379\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:420\u001b[0m, in \u001b[0;36mBaseRetrying._post_stop_check_actions.<locals>.exc_check\u001b[0;34m(rs)\u001b[0m\n\u001b[1;32m    418\u001b[0m retry_exc \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mretry_error_cls(fut)\n\u001b[1;32m    419\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mreraise:\n\u001b[0;32m--> 420\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[43mretry_exc\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreraise\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    421\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m retry_exc \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mfut\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexception\u001b[39;00m()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:187\u001b[0m, in \u001b[0;36mRetryError.reraise\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mreraise\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m t\u001b[38;5;241m.\u001b[39mNoReturn:\n\u001b[1;32m    186\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlast_attempt\u001b[38;5;241m.\u001b[39mfailed:\n\u001b[0;32m--> 187\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mlast_attempt\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mresult\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:451\u001b[0m, in \u001b[0;36mFuture.result\u001b[0;34m(self, timeout)\u001b[0m\n\u001b[1;32m    449\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m CancelledError()\n\u001b[1;32m    450\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;241m==\u001b[39m FINISHED:\n\u001b[0;32m--> 451\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m__get_result\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    453\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_condition\u001b[38;5;241m.\u001b[39mwait(timeout)\n\u001b[1;32m    455\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;129;01min\u001b[39;00m [CANCELLED, CANCELLED_AND_NOTIFIED]:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:403\u001b[0m, in \u001b[0;36mFuture.__get_result\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception:\n\u001b[1;32m    402\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 403\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception\n\u001b[1;32m    404\u001b[0m     \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    405\u001b[0m         \u001b[38;5;66;03m# Break a reference cycle with the exception in self._exception\u001b[39;00m\n\u001b[1;32m    406\u001b[0m         \u001b[38;5;28mself\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:480\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    478\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 480\u001b[0m         result \u001b[38;5;241m=\u001b[39m \u001b[43mfn\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    481\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m:  \u001b[38;5;66;03m# noqa: B902\u001b[39;00m\n\u001b[1;32m    482\u001b[0m         retry_state\u001b[38;5;241m.\u001b[39mset_exception(sys\u001b[38;5;241m.\u001b[39mexc_info())  \u001b[38;5;66;03m# type: ignore[arg-type]\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1167\u001b[0m, in \u001b[0;36mBaseApiClient._request_once\u001b[0;34m(self, http_request, stream)\u001b[0m\n\u001b[1;32m   1165\u001b[0m \u001b[38;5;66;03m# If using proj/location, fetch ADC\u001b[39;00m\n\u001b[1;32m   1166\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mvertexai \u001b[38;5;129;01mand\u001b[39;00m (\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlocation):\n\u001b[0;32m-> 1167\u001b[0m   http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAuthorization\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBearer \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_access_token\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1168\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id:\n\u001b[1;32m   1169\u001b[0m     http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mx-goog-user-project\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1170\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id\n\u001b[1;32m   1171\u001b[0m     )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:982\u001b[0m, in \u001b[0;36mBaseApiClient._access_token\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    980\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_sync_auth_lock:\n\u001b[1;32m    981\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials:\n\u001b[0;32m--> 982\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials, project \u001b[38;5;241m=\u001b[39m \u001b[43mload_auth\u001b[49m\u001b[43m(\u001b[49m\u001b[43mproject\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mproject\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    983\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject:\n\u001b[1;32m    984\u001b[0m       \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;241m=\u001b[39m project\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:184\u001b[0m, in \u001b[0;36mload_auth\u001b[0;34m(project)\u001b[0m\n\u001b[1;32m    182\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mload_auth\u001b[39m(\u001b[38;5;241m*\u001b[39m, project: Union[\u001b[38;5;28mstr\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Tuple[Credentials, \u001b[38;5;28mstr\u001b[39m]:\n\u001b[1;32m    183\u001b[0m \u001b[38;5;250m  \u001b[39m\u001b[38;5;124;03m\"\"\"Loads google auth credentials and project id.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 184\u001b[0m   credentials, loaded_project_id \u001b[38;5;241m=\u001b[39m \u001b[43mgoogle\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mauth\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdefault\u001b[49m\u001b[43m(\u001b[49m\u001b[43m  \u001b[49m\u001b[38;5;66;43;03m# type: ignore[no-untyped-call]\u001b[39;49;00m\n\u001b[1;32m    185\u001b[0m \u001b[43m      \u001b[49m\u001b[43mscopes\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhttps://www.googleapis.com/auth/cloud-platform\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    186\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m project:\n\u001b[1;32m    189\u001b[0m     project \u001b[38;5;241m=\u001b[39m loaded_project_id\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:705\u001b[0m, in \u001b[0;36mdefault\u001b[0;34m(scopes, request, quota_project_id, default_scopes)\u001b[0m\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gce_credentials(request, quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[0;32m--> 705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m \u001b[43mchecker\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    706\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m credentials \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    707\u001b[0m         credentials \u001b[38;5;241m=\u001b[39m with_scopes_if_required(\n\u001b[1;32m    708\u001b[0m             credentials, scopes, default_scopes\u001b[38;5;241m=\u001b[39mdefault_scopes\n\u001b[1;32m    709\u001b[0m         )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:701\u001b[0m, in \u001b[0;36mdefault.<locals>.<lambda>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    687\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mgoogle\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mauth\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcredentials\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m CredentialsWithQuotaProject\n\u001b[1;32m    689\u001b[0m explicit_project_id \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[1;32m    690\u001b[0m     environment_vars\u001b[38;5;241m.\u001b[39mPROJECT, os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(environment_vars\u001b[38;5;241m.\u001b[39mLEGACY_PROJECT)\n\u001b[1;32m    691\u001b[0m )\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[1;32m    696\u001b[0m     \u001b[38;5;66;03m# safely set on the returned credentials since requires_scopes will\u001b[39;00m\n\u001b[1;32m    697\u001b[0m     \u001b[38;5;66;03m# guard against setting scopes on user credentials.\u001b[39;00m\n\u001b[1;32m    698\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_explicit_environ_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    699\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gcloud_sdk_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    700\u001b[0m     _get_gae_credentials,\n\u001b[0;32m--> 701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: \u001b[43m_get_gce_credentials\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mquota_project_id\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquota_project_id\u001b[49m\u001b[43m)\u001b[49m,\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[1;32m    705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m checker()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:404\u001b[0m, in \u001b[0;36m_get_gce_credentials\u001b[0;34m(request, quota_project_id)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m request \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    402\u001b[0m     request \u001b[38;5;241m=\u001b[39m google\u001b[38;5;241m.\u001b[39mauth\u001b[38;5;241m.\u001b[39mtransport\u001b[38;5;241m.\u001b[39m_http_client\u001b[38;5;241m.\u001b[39mRequest()\n\u001b[0;32m--> 404\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43m_metadata\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mis_on_gce\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    405\u001b[0m     \u001b[38;5;66;03m# Get the project ID.\u001b[39;00m\n\u001b[1;32m    406\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    407\u001b[0m         project_id \u001b[38;5;241m=\u001b[39m _metadata\u001b[38;5;241m.\u001b[39mget_project_id(request\u001b[38;5;241m=\u001b[39mrequest)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:119\u001b[0m, in \u001b[0;36mis_on_gce\u001b[0;34m(request)\u001b[0m\n\u001b[1;32m    109\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mis_on_gce\u001b[39m(request):\n\u001b[1;32m    110\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the code runs on Google Compute Engine\u001b[39;00m\n\u001b[1;32m    111\u001b[0m \n\u001b[1;32m    112\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    117\u001b[0m \u001b[38;5;124;03m        bool: True if the code runs on Google Compute Engine, False otherwise.\u001b[39;00m\n\u001b[1;32m    118\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 119\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mping\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    120\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m    122\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m os\u001b[38;5;241m.\u001b[39mname \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnt\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m    123\u001b[0m         \u001b[38;5;66;03m# TODO: implement GCE residency detection on Windows\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:186\u001b[0m, in \u001b[0;36mping\u001b[0;34m(request, timeout, retry_count)\u001b[0m\n\u001b[1;32m    173\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mping\u001b[39m(request, timeout\u001b[38;5;241m=\u001b[39m_METADATA_DEFAULT_TIMEOUT, retry_count\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3\u001b[39m):\n\u001b[1;32m    174\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the metadata server is available.\u001b[39;00m\n\u001b[1;32m    175\u001b[0m \n\u001b[1;32m    176\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m        bool: True if the metadata server is reachable, False otherwise.\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 186\u001b[0m     use_mtls \u001b[38;5;241m=\u001b[39m \u001b[43m_mtls\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mshould_use_mds_mtls\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    187\u001b[0m     _prepare_request_for_mds(request, use_mtls\u001b[38;5;241m=\u001b[39muse_mtls)\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;66;03m# NOTE: The explicit ``timeout`` is a workaround. The underlying\u001b[39;00m\n\u001b[1;32m    189\u001b[0m     \u001b[38;5;66;03m#       issue is that resolving an unknown host on some networks will take\u001b[39;00m\n\u001b[1;32m    190\u001b[0m     \u001b[38;5;66;03m#       20-30 seconds; making this timeout short fixes the issue, but\u001b[39;00m\n\u001b[1;32m    191\u001b[0m     \u001b[38;5;66;03m#       could lead to false negatives in the event that we are on GCE, but\u001b[39;00m\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m#       the metadata resolution was particularly slow. The latter case is\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;66;03m#       \"unlikely\".\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:103\u001b[0m, in \u001b[0;36mshould_use_mds_mtls\u001b[0;34m(mds_mtls_config)\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mshould_use_mds_mtls\u001b[39m(mds_mtls_config: MdsMtlsConfig \u001b[38;5;241m=\u001b[39m MdsMtlsConfig()):\n\u001b[1;32m    102\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Determines if mTLS should be used for the metadata server.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 103\u001b[0m     mode \u001b[38;5;241m=\u001b[39m \u001b[43m_parse_mds_mode\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m mode \u001b[38;5;241m==\u001b[39m MdsMtlsMode\u001b[38;5;241m.\u001b[39mSTRICT:\n\u001b[1;32m    105\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _certs_exist(mds_mtls_config):\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:91\u001b[0m, in \u001b[0;36m_parse_mds_mode\u001b[0;34m()\u001b[0m\n\u001b[1;32m     88\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_parse_mds_mode\u001b[39m():\n\u001b[1;32m     89\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Parses the GCE_METADATA_MTLS_MODE environment variable.\"\"\"\u001b[39;00m\n\u001b[1;32m     90\u001b[0m     mode_str \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[0;32m---> 91\u001b[0m         \u001b[43menvironment_vars\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mGCE_METADATA_MTLS_MODE\u001b[49m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdefault\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     92\u001b[0m     )\u001b[38;5;241m.\u001b[39mlower()\n\u001b[1;32m     93\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m     94\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m MdsMtlsMode(mode_str)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'"
     ]
    }
   ],
   "source": [
    "sheet_music_pdf_uri = \"gs://github-repo/use-cases/sheet-music/24ItalianSongs.pdf\"\n",
    "\n",
    "sheet_music_extraction_prompt = \"\"\"The following document is a book of sheet music. Your task is to output structured metadata about every piece of music in the document.\n",
    "\n",
    "Correct any mistakes that are in the document and fill in missing information when not present in the document.\n",
    "\n",
    "Include the following details:\n",
    "\n",
    "Title\n",
    "Composer with lifetime\n",
    "Tempo Marking\n",
    "A description of the piece\n",
    "\"\"\"\n",
    "\n",
    "# Send to Gemini\n",
    "response = client.models.generate_content(\n",
    "    model=MODEL_ID,\n",
    "    contents=[\n",
    "        sheet_music_extraction_prompt,\n",
    "        # Load file directly from Google Cloud Storage\n",
    "        Part.from_uri(\n",
    "            file_uri=sheet_music_pdf_uri,\n",
    "            mime_type=\"application/pdf\",\n",
    "        ),\n",
    "    ],\n",
    "    config=config,\n",
    ")\n",
    "\n",
    "# Display results\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "29b40b5e0cb0"
   },
   "source": [
    "You can see that Gemini extracted all of the relevant fields from the document."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "db3765c7645d"
   },
   "source": [
    "### Song Identification with Audio\n",
    "\n",
    "Now, let's try something more challenging, identifying a song being performed based on the sheet music. We have an audio clip of Holt Skinner performing one of the songs in the book, and we will ask Gemini to identify it based on the sheet music PDF."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "61ea3f2f1c4a"
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[7], line 15\u001b[0m\n\u001b[1;32m      9\u001b[0m audio_part \u001b[38;5;241m=\u001b[39m Part\u001b[38;5;241m.\u001b[39mfrom_uri(\n\u001b[1;32m     10\u001b[0m     file_uri\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgs://github-repo/use-cases/sheet-music/24ItalianClip.mp3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     11\u001b[0m     mime_type\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maudio/mpeg\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     12\u001b[0m )\n\u001b[1;32m     14\u001b[0m \u001b[38;5;66;03m# Send to Gemini\u001b[39;00m\n\u001b[0;32m---> 15\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmodels\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgenerate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m     16\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mMODEL_ID\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     17\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[43mpdf_part\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maudio_part\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msong_identification_prompt\u001b[49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     18\u001b[0m \u001b[43m    \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mconfig\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     19\u001b[0m \u001b[43m)\u001b[49m\n\u001b[1;32m     21\u001b[0m \u001b[38;5;66;03m# Display results\u001b[39;00m\n\u001b[1;32m     22\u001b[0m display(Markdown(response\u001b[38;5;241m.\u001b[39mtext))\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:5203\u001b[0m, in \u001b[0;36mModels.generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   5201\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m remaining_remote_calls_afc \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[1;32m   5202\u001b[0m   i \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[0;32m-> 5203\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_generate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   5204\u001b[0m \u001b[43m      \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmodel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcontents\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparsed_config\u001b[49m\n\u001b[1;32m   5205\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   5207\u001b[0m   function_map \u001b[38;5;241m=\u001b[39m _extra_utils\u001b[38;5;241m.\u001b[39mget_function_map(parsed_config)\n\u001b[1;32m   5208\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m function_map:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:3985\u001b[0m, in \u001b[0;36mModels._generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   3982\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mconvert_to_dict(request_dict)\n\u001b[1;32m   3983\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mencode_unserializable_types(request_dict)\n\u001b[0;32m-> 3985\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_api_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   3986\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mpost\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpath\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_dict\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\n\u001b[1;32m   3987\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   3989\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m config \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(\n\u001b[1;32m   3990\u001b[0m     config, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mshould_return_http_response\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   3991\u001b[0m ):\n\u001b[1;32m   3992\u001b[0m   return_value \u001b[38;5;241m=\u001b[39m types\u001b[38;5;241m.\u001b[39mGenerateContentResponse(sdk_http_response\u001b[38;5;241m=\u001b[39mresponse)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1388\u001b[0m, in \u001b[0;36mBaseApiClient.request\u001b[0;34m(self, http_method, path, request_dict, http_options)\u001b[0m\n\u001b[1;32m   1378\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mrequest\u001b[39m(\n\u001b[1;32m   1379\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m   1380\u001b[0m     http_method: \u001b[38;5;28mstr\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m   1383\u001b[0m     http_options: Optional[HttpOptionsOrDict] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m   1384\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m SdkHttpResponse:\n\u001b[1;32m   1385\u001b[0m   http_request \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_build_request(\n\u001b[1;32m   1386\u001b[0m       http_method, path, request_dict, http_options\n\u001b[1;32m   1387\u001b[0m   )\n\u001b[0;32m-> 1388\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[1;32m   1389\u001b[0m   response_body \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1390\u001b[0m       response\u001b[38;5;241m.\u001b[39mresponse_stream[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mresponse_stream \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1391\u001b[0m   )\n\u001b[1;32m   1392\u001b[0m   \u001b[38;5;28;01mreturn\u001b[39;00m SdkHttpResponse(headers\u001b[38;5;241m=\u001b[39mresponse\u001b[38;5;241m.\u001b[39mheaders, body\u001b[38;5;241m=\u001b[39mresponse_body)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1224\u001b[0m, in \u001b[0;36mBaseApiClient._request\u001b[0;34m(self, http_request, http_options, stream)\u001b[0m\n\u001b[1;32m   1221\u001b[0m     retry \u001b[38;5;241m=\u001b[39m tenacity\u001b[38;5;241m.\u001b[39mRetrying(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mretry_kwargs)\n\u001b[1;32m   1222\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m retry(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_request_once, http_request, stream)  \u001b[38;5;66;03m# type: ignore[no-any-return]\u001b[39;00m\n\u001b[0;32m-> 1224\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_retry\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request_once\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:477\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    475\u001b[0m retry_state \u001b[38;5;241m=\u001b[39m RetryCallState(retry_object\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m, fn\u001b[38;5;241m=\u001b[39mfn, args\u001b[38;5;241m=\u001b[39margs, kwargs\u001b[38;5;241m=\u001b[39mkwargs)\n\u001b[1;32m    476\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m--> 477\u001b[0m     do \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43miter\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    478\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m         \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:378\u001b[0m, in \u001b[0;36mBaseRetrying.iter\u001b[0;34m(self, retry_state)\u001b[0m\n\u001b[1;32m    376\u001b[0m result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m    377\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m action \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39miter_state\u001b[38;5;241m.\u001b[39mactions:\n\u001b[0;32m--> 378\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43maction\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    379\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:420\u001b[0m, in \u001b[0;36mBaseRetrying._post_stop_check_actions.<locals>.exc_check\u001b[0;34m(rs)\u001b[0m\n\u001b[1;32m    418\u001b[0m retry_exc \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mretry_error_cls(fut)\n\u001b[1;32m    419\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mreraise:\n\u001b[0;32m--> 420\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[43mretry_exc\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreraise\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    421\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m retry_exc \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mfut\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexception\u001b[39;00m()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:187\u001b[0m, in \u001b[0;36mRetryError.reraise\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mreraise\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m t\u001b[38;5;241m.\u001b[39mNoReturn:\n\u001b[1;32m    186\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlast_attempt\u001b[38;5;241m.\u001b[39mfailed:\n\u001b[0;32m--> 187\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mlast_attempt\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mresult\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:451\u001b[0m, in \u001b[0;36mFuture.result\u001b[0;34m(self, timeout)\u001b[0m\n\u001b[1;32m    449\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m CancelledError()\n\u001b[1;32m    450\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;241m==\u001b[39m FINISHED:\n\u001b[0;32m--> 451\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m__get_result\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    453\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_condition\u001b[38;5;241m.\u001b[39mwait(timeout)\n\u001b[1;32m    455\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;129;01min\u001b[39;00m [CANCELLED, CANCELLED_AND_NOTIFIED]:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:403\u001b[0m, in \u001b[0;36mFuture.__get_result\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception:\n\u001b[1;32m    402\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 403\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception\n\u001b[1;32m    404\u001b[0m     \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    405\u001b[0m         \u001b[38;5;66;03m# Break a reference cycle with the exception in self._exception\u001b[39;00m\n\u001b[1;32m    406\u001b[0m         \u001b[38;5;28mself\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:480\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    478\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 480\u001b[0m         result \u001b[38;5;241m=\u001b[39m \u001b[43mfn\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    481\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m:  \u001b[38;5;66;03m# noqa: B902\u001b[39;00m\n\u001b[1;32m    482\u001b[0m         retry_state\u001b[38;5;241m.\u001b[39mset_exception(sys\u001b[38;5;241m.\u001b[39mexc_info())  \u001b[38;5;66;03m# type: ignore[arg-type]\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1167\u001b[0m, in \u001b[0;36mBaseApiClient._request_once\u001b[0;34m(self, http_request, stream)\u001b[0m\n\u001b[1;32m   1165\u001b[0m \u001b[38;5;66;03m# If using proj/location, fetch ADC\u001b[39;00m\n\u001b[1;32m   1166\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mvertexai \u001b[38;5;129;01mand\u001b[39;00m (\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlocation):\n\u001b[0;32m-> 1167\u001b[0m   http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAuthorization\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBearer \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_access_token\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1168\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id:\n\u001b[1;32m   1169\u001b[0m     http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mx-goog-user-project\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1170\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id\n\u001b[1;32m   1171\u001b[0m     )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:982\u001b[0m, in \u001b[0;36mBaseApiClient._access_token\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    980\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_sync_auth_lock:\n\u001b[1;32m    981\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials:\n\u001b[0;32m--> 982\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials, project \u001b[38;5;241m=\u001b[39m \u001b[43mload_auth\u001b[49m\u001b[43m(\u001b[49m\u001b[43mproject\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mproject\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    983\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject:\n\u001b[1;32m    984\u001b[0m       \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;241m=\u001b[39m project\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:184\u001b[0m, in \u001b[0;36mload_auth\u001b[0;34m(project)\u001b[0m\n\u001b[1;32m    182\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mload_auth\u001b[39m(\u001b[38;5;241m*\u001b[39m, project: Union[\u001b[38;5;28mstr\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Tuple[Credentials, \u001b[38;5;28mstr\u001b[39m]:\n\u001b[1;32m    183\u001b[0m \u001b[38;5;250m  \u001b[39m\u001b[38;5;124;03m\"\"\"Loads google auth credentials and project id.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 184\u001b[0m   credentials, loaded_project_id \u001b[38;5;241m=\u001b[39m \u001b[43mgoogle\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mauth\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdefault\u001b[49m\u001b[43m(\u001b[49m\u001b[43m  \u001b[49m\u001b[38;5;66;43;03m# type: ignore[no-untyped-call]\u001b[39;49;00m\n\u001b[1;32m    185\u001b[0m \u001b[43m      \u001b[49m\u001b[43mscopes\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhttps://www.googleapis.com/auth/cloud-platform\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    186\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m project:\n\u001b[1;32m    189\u001b[0m     project \u001b[38;5;241m=\u001b[39m loaded_project_id\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:705\u001b[0m, in \u001b[0;36mdefault\u001b[0;34m(scopes, request, quota_project_id, default_scopes)\u001b[0m\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gce_credentials(request, quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[0;32m--> 705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m \u001b[43mchecker\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    706\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m credentials \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    707\u001b[0m         credentials \u001b[38;5;241m=\u001b[39m with_scopes_if_required(\n\u001b[1;32m    708\u001b[0m             credentials, scopes, default_scopes\u001b[38;5;241m=\u001b[39mdefault_scopes\n\u001b[1;32m    709\u001b[0m         )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:701\u001b[0m, in \u001b[0;36mdefault.<locals>.<lambda>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    687\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mgoogle\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mauth\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcredentials\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m CredentialsWithQuotaProject\n\u001b[1;32m    689\u001b[0m explicit_project_id \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[1;32m    690\u001b[0m     environment_vars\u001b[38;5;241m.\u001b[39mPROJECT, os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(environment_vars\u001b[38;5;241m.\u001b[39mLEGACY_PROJECT)\n\u001b[1;32m    691\u001b[0m )\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[1;32m    696\u001b[0m     \u001b[38;5;66;03m# safely set on the returned credentials since requires_scopes will\u001b[39;00m\n\u001b[1;32m    697\u001b[0m     \u001b[38;5;66;03m# guard against setting scopes on user credentials.\u001b[39;00m\n\u001b[1;32m    698\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_explicit_environ_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    699\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gcloud_sdk_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    700\u001b[0m     _get_gae_credentials,\n\u001b[0;32m--> 701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: \u001b[43m_get_gce_credentials\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mquota_project_id\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquota_project_id\u001b[49m\u001b[43m)\u001b[49m,\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[1;32m    705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m checker()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:404\u001b[0m, in \u001b[0;36m_get_gce_credentials\u001b[0;34m(request, quota_project_id)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m request \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    402\u001b[0m     request \u001b[38;5;241m=\u001b[39m google\u001b[38;5;241m.\u001b[39mauth\u001b[38;5;241m.\u001b[39mtransport\u001b[38;5;241m.\u001b[39m_http_client\u001b[38;5;241m.\u001b[39mRequest()\n\u001b[0;32m--> 404\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43m_metadata\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mis_on_gce\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    405\u001b[0m     \u001b[38;5;66;03m# Get the project ID.\u001b[39;00m\n\u001b[1;32m    406\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    407\u001b[0m         project_id \u001b[38;5;241m=\u001b[39m _metadata\u001b[38;5;241m.\u001b[39mget_project_id(request\u001b[38;5;241m=\u001b[39mrequest)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:119\u001b[0m, in \u001b[0;36mis_on_gce\u001b[0;34m(request)\u001b[0m\n\u001b[1;32m    109\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mis_on_gce\u001b[39m(request):\n\u001b[1;32m    110\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the code runs on Google Compute Engine\u001b[39;00m\n\u001b[1;32m    111\u001b[0m \n\u001b[1;32m    112\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    117\u001b[0m \u001b[38;5;124;03m        bool: True if the code runs on Google Compute Engine, False otherwise.\u001b[39;00m\n\u001b[1;32m    118\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 119\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mping\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    120\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m    122\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m os\u001b[38;5;241m.\u001b[39mname \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnt\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m    123\u001b[0m         \u001b[38;5;66;03m# TODO: implement GCE residency detection on Windows\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:186\u001b[0m, in \u001b[0;36mping\u001b[0;34m(request, timeout, retry_count)\u001b[0m\n\u001b[1;32m    173\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mping\u001b[39m(request, timeout\u001b[38;5;241m=\u001b[39m_METADATA_DEFAULT_TIMEOUT, retry_count\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3\u001b[39m):\n\u001b[1;32m    174\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the metadata server is available.\u001b[39;00m\n\u001b[1;32m    175\u001b[0m \n\u001b[1;32m    176\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m        bool: True if the metadata server is reachable, False otherwise.\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 186\u001b[0m     use_mtls \u001b[38;5;241m=\u001b[39m \u001b[43m_mtls\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mshould_use_mds_mtls\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    187\u001b[0m     _prepare_request_for_mds(request, use_mtls\u001b[38;5;241m=\u001b[39muse_mtls)\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;66;03m# NOTE: The explicit ``timeout`` is a workaround. The underlying\u001b[39;00m\n\u001b[1;32m    189\u001b[0m     \u001b[38;5;66;03m#       issue is that resolving an unknown host on some networks will take\u001b[39;00m\n\u001b[1;32m    190\u001b[0m     \u001b[38;5;66;03m#       20-30 seconds; making this timeout short fixes the issue, but\u001b[39;00m\n\u001b[1;32m    191\u001b[0m     \u001b[38;5;66;03m#       could lead to false negatives in the event that we are on GCE, but\u001b[39;00m\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m#       the metadata resolution was particularly slow. The latter case is\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;66;03m#       \"unlikely\".\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:103\u001b[0m, in \u001b[0;36mshould_use_mds_mtls\u001b[0;34m(mds_mtls_config)\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mshould_use_mds_mtls\u001b[39m(mds_mtls_config: MdsMtlsConfig \u001b[38;5;241m=\u001b[39m MdsMtlsConfig()):\n\u001b[1;32m    102\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Determines if mTLS should be used for the metadata server.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 103\u001b[0m     mode \u001b[38;5;241m=\u001b[39m \u001b[43m_parse_mds_mode\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m mode \u001b[38;5;241m==\u001b[39m MdsMtlsMode\u001b[38;5;241m.\u001b[39mSTRICT:\n\u001b[1;32m    105\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _certs_exist(mds_mtls_config):\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:91\u001b[0m, in \u001b[0;36m_parse_mds_mode\u001b[0;34m()\u001b[0m\n\u001b[1;32m     88\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_parse_mds_mode\u001b[39m():\n\u001b[1;32m     89\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Parses the GCE_METADATA_MTLS_MODE environment variable.\"\"\"\u001b[39;00m\n\u001b[1;32m     90\u001b[0m     mode_str \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[0;32m---> 91\u001b[0m         \u001b[43menvironment_vars\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mGCE_METADATA_MTLS_MODE\u001b[49m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdefault\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     92\u001b[0m     )\u001b[38;5;241m.\u001b[39mlower()\n\u001b[1;32m     93\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m     94\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m MdsMtlsMode(mode_str)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'"
     ]
    }
   ],
   "source": [
    "song_identification_prompt = \"\"\"Based on the sheet music PDF, what song is in the audio clip? Explain how you made the decision.\"\"\"\n",
    "\n",
    "# Load PDF file\n",
    "pdf_part = Part.from_uri(\n",
    "    file_uri=sheet_music_pdf_uri,\n",
    "    mime_type=\"application/pdf\",\n",
    ")\n",
    "\n",
    "audio_part = Part.from_uri(\n",
    "    file_uri=\"gs://github-repo/use-cases/sheet-music/24ItalianClip.mp3\",\n",
    "    mime_type=\"audio/mpeg\",\n",
    ")\n",
    "\n",
    "# Send to Gemini\n",
    "response = client.models.generate_content(\n",
    "    model=MODEL_ID,\n",
    "    contents=[pdf_part, audio_part, song_identification_prompt],\n",
    "    config=config,\n",
    ")\n",
    "\n",
    "# Display results\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "9730e8a5628b"
   },
   "source": [
    "### Edit PDF Metadata\n",
    "\n",
    "Next, we'll use the output from Gemini to edit the metadata of a PDF containing one song, which can make it easier to organize this file in sheet music applications.\n",
    "\n",
    "We'll adjust the prompt slightly and set the [`response_mime_type`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini#:~:text=in%20the%20list.-,responseMimeType,-(Preview)) to get the response in JSON format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "97e2a06cc762"
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[8], line 24\u001b[0m\n\u001b[1;32m     21\u001b[0m temp_config \u001b[38;5;241m=\u001b[39m config\u001b[38;5;241m.\u001b[39mmodel_copy()\n\u001b[1;32m     23\u001b[0m \u001b[38;5;66;03m# Send to Gemini\u001b[39;00m\n\u001b[0;32m---> 24\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[43mclient\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmodels\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgenerate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m     25\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mMODEL_ID\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     26\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[43msheet_music_extraction_prompt\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfile_part\u001b[49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     27\u001b[0m \u001b[43m    \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mtemp_config\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m     28\u001b[0m \u001b[43m)\u001b[49m\n\u001b[1;32m     30\u001b[0m raw_text \u001b[38;5;241m=\u001b[39m response\u001b[38;5;241m.\u001b[39mtext\u001b[38;5;241m.\u001b[39mstrip()\n\u001b[1;32m     32\u001b[0m start \u001b[38;5;241m=\u001b[39m raw_text\u001b[38;5;241m.\u001b[39mfind(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:5203\u001b[0m, in \u001b[0;36mModels.generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   5201\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m remaining_remote_calls_afc \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[1;32m   5202\u001b[0m   i \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[0;32m-> 5203\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_generate_content\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   5204\u001b[0m \u001b[43m      \u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mmodel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontents\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mcontents\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconfig\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparsed_config\u001b[49m\n\u001b[1;32m   5205\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   5207\u001b[0m   function_map \u001b[38;5;241m=\u001b[39m _extra_utils\u001b[38;5;241m.\u001b[39mget_function_map(parsed_config)\n\u001b[1;32m   5208\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m function_map:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/models.py:3985\u001b[0m, in \u001b[0;36mModels._generate_content\u001b[0;34m(self, model, contents, config)\u001b[0m\n\u001b[1;32m   3982\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mconvert_to_dict(request_dict)\n\u001b[1;32m   3983\u001b[0m request_dict \u001b[38;5;241m=\u001b[39m _common\u001b[38;5;241m.\u001b[39mencode_unserializable_types(request_dict)\n\u001b[0;32m-> 3985\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_api_client\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   3986\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mpost\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpath\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_dict\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\n\u001b[1;32m   3987\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   3989\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m config \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(\n\u001b[1;32m   3990\u001b[0m     config, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mshould_return_http_response\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   3991\u001b[0m ):\n\u001b[1;32m   3992\u001b[0m   return_value \u001b[38;5;241m=\u001b[39m types\u001b[38;5;241m.\u001b[39mGenerateContentResponse(sdk_http_response\u001b[38;5;241m=\u001b[39mresponse)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1388\u001b[0m, in \u001b[0;36mBaseApiClient.request\u001b[0;34m(self, http_method, path, request_dict, http_options)\u001b[0m\n\u001b[1;32m   1378\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mrequest\u001b[39m(\n\u001b[1;32m   1379\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m   1380\u001b[0m     http_method: \u001b[38;5;28mstr\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m   1383\u001b[0m     http_options: Optional[HttpOptionsOrDict] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m   1384\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m SdkHttpResponse:\n\u001b[1;32m   1385\u001b[0m   http_request \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_build_request(\n\u001b[1;32m   1386\u001b[0m       http_method, path, request_dict, http_options\n\u001b[1;32m   1387\u001b[0m   )\n\u001b[0;32m-> 1388\u001b[0m   response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_options\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[1;32m   1389\u001b[0m   response_body \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1390\u001b[0m       response\u001b[38;5;241m.\u001b[39mresponse_stream[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mif\u001b[39;00m response\u001b[38;5;241m.\u001b[39mresponse_stream \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1391\u001b[0m   )\n\u001b[1;32m   1392\u001b[0m   \u001b[38;5;28;01mreturn\u001b[39;00m SdkHttpResponse(headers\u001b[38;5;241m=\u001b[39mresponse\u001b[38;5;241m.\u001b[39mheaders, body\u001b[38;5;241m=\u001b[39mresponse_body)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1224\u001b[0m, in \u001b[0;36mBaseApiClient._request\u001b[0;34m(self, http_request, http_options, stream)\u001b[0m\n\u001b[1;32m   1221\u001b[0m     retry \u001b[38;5;241m=\u001b[39m tenacity\u001b[38;5;241m.\u001b[39mRetrying(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mretry_kwargs)\n\u001b[1;32m   1222\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m retry(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_request_once, http_request, stream)  \u001b[38;5;66;03m# type: ignore[no-any-return]\u001b[39;00m\n\u001b[0;32m-> 1224\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_retry\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_request_once\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhttp_request\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:477\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    475\u001b[0m retry_state \u001b[38;5;241m=\u001b[39m RetryCallState(retry_object\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m, fn\u001b[38;5;241m=\u001b[39mfn, args\u001b[38;5;241m=\u001b[39margs, kwargs\u001b[38;5;241m=\u001b[39mkwargs)\n\u001b[1;32m    476\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m--> 477\u001b[0m     do \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43miter\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    478\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m         \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:378\u001b[0m, in \u001b[0;36mBaseRetrying.iter\u001b[0;34m(self, retry_state)\u001b[0m\n\u001b[1;32m    376\u001b[0m result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m    377\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m action \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39miter_state\u001b[38;5;241m.\u001b[39mactions:\n\u001b[0;32m--> 378\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43maction\u001b[49m\u001b[43m(\u001b[49m\u001b[43mretry_state\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    379\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:420\u001b[0m, in \u001b[0;36mBaseRetrying._post_stop_check_actions.<locals>.exc_check\u001b[0;34m(rs)\u001b[0m\n\u001b[1;32m    418\u001b[0m retry_exc \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mretry_error_cls(fut)\n\u001b[1;32m    419\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mreraise:\n\u001b[0;32m--> 420\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[43mretry_exc\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mreraise\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    421\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m retry_exc \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mfut\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexception\u001b[39;00m()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:187\u001b[0m, in \u001b[0;36mRetryError.reraise\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mreraise\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m t\u001b[38;5;241m.\u001b[39mNoReturn:\n\u001b[1;32m    186\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlast_attempt\u001b[38;5;241m.\u001b[39mfailed:\n\u001b[0;32m--> 187\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mlast_attempt\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mresult\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:451\u001b[0m, in \u001b[0;36mFuture.result\u001b[0;34m(self, timeout)\u001b[0m\n\u001b[1;32m    449\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m CancelledError()\n\u001b[1;32m    450\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;241m==\u001b[39m FINISHED:\n\u001b[0;32m--> 451\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m__get_result\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    453\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_condition\u001b[38;5;241m.\u001b[39mwait(timeout)\n\u001b[1;32m    455\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;129;01min\u001b[39;00m [CANCELLED, CANCELLED_AND_NOTIFIED]:\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/concurrent/futures/_base.py:403\u001b[0m, in \u001b[0;36mFuture.__get_result\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception:\n\u001b[1;32m    402\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 403\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception\n\u001b[1;32m    404\u001b[0m     \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[1;32m    405\u001b[0m         \u001b[38;5;66;03m# Break a reference cycle with the exception in self._exception\u001b[39;00m\n\u001b[1;32m    406\u001b[0m         \u001b[38;5;28mself\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/tenacity/__init__.py:480\u001b[0m, in \u001b[0;36mRetrying.__call__\u001b[0;34m(self, fn, *args, **kwargs)\u001b[0m\n\u001b[1;32m    478\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(do, DoAttempt):\n\u001b[1;32m    479\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 480\u001b[0m         result \u001b[38;5;241m=\u001b[39m \u001b[43mfn\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    481\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m:  \u001b[38;5;66;03m# noqa: B902\u001b[39;00m\n\u001b[1;32m    482\u001b[0m         retry_state\u001b[38;5;241m.\u001b[39mset_exception(sys\u001b[38;5;241m.\u001b[39mexc_info())  \u001b[38;5;66;03m# type: ignore[arg-type]\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:1167\u001b[0m, in \u001b[0;36mBaseApiClient._request_once\u001b[0;34m(self, http_request, stream)\u001b[0m\n\u001b[1;32m   1165\u001b[0m \u001b[38;5;66;03m# If using proj/location, fetch ADC\u001b[39;00m\n\u001b[1;32m   1166\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mvertexai \u001b[38;5;129;01mand\u001b[39;00m (\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlocation):\n\u001b[0;32m-> 1167\u001b[0m   http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAuthorization\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBearer \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_access_token\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m   1168\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id:\n\u001b[1;32m   1169\u001b[0m     http_request\u001b[38;5;241m.\u001b[39mheaders[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mx-goog-user-project\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m   1170\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials\u001b[38;5;241m.\u001b[39mquota_project_id\n\u001b[1;32m   1171\u001b[0m     )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:982\u001b[0m, in \u001b[0;36mBaseApiClient._access_token\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    980\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_sync_auth_lock:\n\u001b[1;32m    981\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials:\n\u001b[0;32m--> 982\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_credentials, project \u001b[38;5;241m=\u001b[39m \u001b[43mload_auth\u001b[49m\u001b[43m(\u001b[49m\u001b[43mproject\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mproject\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    983\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject:\n\u001b[1;32m    984\u001b[0m       \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproject \u001b[38;5;241m=\u001b[39m project\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/genai/_api_client.py:184\u001b[0m, in \u001b[0;36mload_auth\u001b[0;34m(project)\u001b[0m\n\u001b[1;32m    182\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mload_auth\u001b[39m(\u001b[38;5;241m*\u001b[39m, project: Union[\u001b[38;5;28mstr\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m]) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Tuple[Credentials, \u001b[38;5;28mstr\u001b[39m]:\n\u001b[1;32m    183\u001b[0m \u001b[38;5;250m  \u001b[39m\u001b[38;5;124;03m\"\"\"Loads google auth credentials and project id.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 184\u001b[0m   credentials, loaded_project_id \u001b[38;5;241m=\u001b[39m \u001b[43mgoogle\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mauth\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdefault\u001b[49m\u001b[43m(\u001b[49m\u001b[43m  \u001b[49m\u001b[38;5;66;43;03m# type: ignore[no-untyped-call]\u001b[39;49;00m\n\u001b[1;32m    185\u001b[0m \u001b[43m      \u001b[49m\u001b[43mscopes\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhttps://www.googleapis.com/auth/cloud-platform\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    186\u001b[0m \u001b[43m  \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    188\u001b[0m   \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m project:\n\u001b[1;32m    189\u001b[0m     project \u001b[38;5;241m=\u001b[39m loaded_project_id\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:705\u001b[0m, in \u001b[0;36mdefault\u001b[0;34m(scopes, request, quota_project_id, default_scopes)\u001b[0m\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gce_credentials(request, quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[0;32m--> 705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m \u001b[43mchecker\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    706\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m credentials \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    707\u001b[0m         credentials \u001b[38;5;241m=\u001b[39m with_scopes_if_required(\n\u001b[1;32m    708\u001b[0m             credentials, scopes, default_scopes\u001b[38;5;241m=\u001b[39mdefault_scopes\n\u001b[1;32m    709\u001b[0m         )\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:701\u001b[0m, in \u001b[0;36mdefault.<locals>.<lambda>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    687\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mgoogle\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mauth\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcredentials\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m CredentialsWithQuotaProject\n\u001b[1;32m    689\u001b[0m explicit_project_id \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[1;32m    690\u001b[0m     environment_vars\u001b[38;5;241m.\u001b[39mPROJECT, os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(environment_vars\u001b[38;5;241m.\u001b[39mLEGACY_PROJECT)\n\u001b[1;32m    691\u001b[0m )\n\u001b[1;32m    693\u001b[0m checkers \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    694\u001b[0m     \u001b[38;5;66;03m# Avoid passing scopes here to prevent passing scopes to user credentials.\u001b[39;00m\n\u001b[1;32m    695\u001b[0m     \u001b[38;5;66;03m# with_scopes_if_required() below will ensure scopes/default scopes are\u001b[39;00m\n\u001b[1;32m    696\u001b[0m     \u001b[38;5;66;03m# safely set on the returned credentials since requires_scopes will\u001b[39;00m\n\u001b[1;32m    697\u001b[0m     \u001b[38;5;66;03m# guard against setting scopes on user credentials.\u001b[39;00m\n\u001b[1;32m    698\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_explicit_environ_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    699\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: _get_gcloud_sdk_credentials(quota_project_id\u001b[38;5;241m=\u001b[39mquota_project_id),\n\u001b[1;32m    700\u001b[0m     _get_gae_credentials,\n\u001b[0;32m--> 701\u001b[0m     \u001b[38;5;28;01mlambda\u001b[39;00m: \u001b[43m_get_gce_credentials\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mquota_project_id\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquota_project_id\u001b[49m\u001b[43m)\u001b[49m,\n\u001b[1;32m    702\u001b[0m )\n\u001b[1;32m    704\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m checker \u001b[38;5;129;01min\u001b[39;00m checkers:\n\u001b[1;32m    705\u001b[0m     credentials, project_id \u001b[38;5;241m=\u001b[39m checker()\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/_default.py:404\u001b[0m, in \u001b[0;36m_get_gce_credentials\u001b[0;34m(request, quota_project_id)\u001b[0m\n\u001b[1;32m    401\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m request \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    402\u001b[0m     request \u001b[38;5;241m=\u001b[39m google\u001b[38;5;241m.\u001b[39mauth\u001b[38;5;241m.\u001b[39mtransport\u001b[38;5;241m.\u001b[39m_http_client\u001b[38;5;241m.\u001b[39mRequest()\n\u001b[0;32m--> 404\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43m_metadata\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mis_on_gce\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    405\u001b[0m     \u001b[38;5;66;03m# Get the project ID.\u001b[39;00m\n\u001b[1;32m    406\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m    407\u001b[0m         project_id \u001b[38;5;241m=\u001b[39m _metadata\u001b[38;5;241m.\u001b[39mget_project_id(request\u001b[38;5;241m=\u001b[39mrequest)\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:119\u001b[0m, in \u001b[0;36mis_on_gce\u001b[0;34m(request)\u001b[0m\n\u001b[1;32m    109\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mis_on_gce\u001b[39m(request):\n\u001b[1;32m    110\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the code runs on Google Compute Engine\u001b[39;00m\n\u001b[1;32m    111\u001b[0m \n\u001b[1;32m    112\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    117\u001b[0m \u001b[38;5;124;03m        bool: True if the code runs on Google Compute Engine, False otherwise.\u001b[39;00m\n\u001b[1;32m    118\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 119\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[43mping\u001b[49m\u001b[43m(\u001b[49m\u001b[43mrequest\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[1;32m    120\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[1;32m    122\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m os\u001b[38;5;241m.\u001b[39mname \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnt\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m    123\u001b[0m         \u001b[38;5;66;03m# TODO: implement GCE residency detection on Windows\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_metadata.py:186\u001b[0m, in \u001b[0;36mping\u001b[0;34m(request, timeout, retry_count)\u001b[0m\n\u001b[1;32m    173\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mping\u001b[39m(request, timeout\u001b[38;5;241m=\u001b[39m_METADATA_DEFAULT_TIMEOUT, retry_count\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3\u001b[39m):\n\u001b[1;32m    174\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Checks to see if the metadata server is available.\u001b[39;00m\n\u001b[1;32m    175\u001b[0m \n\u001b[1;32m    176\u001b[0m \u001b[38;5;124;03m    Args:\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;124;03m        bool: True if the metadata server is reachable, False otherwise.\u001b[39;00m\n\u001b[1;32m    185\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 186\u001b[0m     use_mtls \u001b[38;5;241m=\u001b[39m \u001b[43m_mtls\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mshould_use_mds_mtls\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    187\u001b[0m     _prepare_request_for_mds(request, use_mtls\u001b[38;5;241m=\u001b[39muse_mtls)\n\u001b[1;32m    188\u001b[0m     \u001b[38;5;66;03m# NOTE: The explicit ``timeout`` is a workaround. The underlying\u001b[39;00m\n\u001b[1;32m    189\u001b[0m     \u001b[38;5;66;03m#       issue is that resolving an unknown host on some networks will take\u001b[39;00m\n\u001b[1;32m    190\u001b[0m     \u001b[38;5;66;03m#       20-30 seconds; making this timeout short fixes the issue, but\u001b[39;00m\n\u001b[1;32m    191\u001b[0m     \u001b[38;5;66;03m#       could lead to false negatives in the event that we are on GCE, but\u001b[39;00m\n\u001b[1;32m    192\u001b[0m     \u001b[38;5;66;03m#       the metadata resolution was particularly slow. The latter case is\u001b[39;00m\n\u001b[1;32m    193\u001b[0m     \u001b[38;5;66;03m#       \"unlikely\".\u001b[39;00m\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:103\u001b[0m, in \u001b[0;36mshould_use_mds_mtls\u001b[0;34m(mds_mtls_config)\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21mshould_use_mds_mtls\u001b[39m(mds_mtls_config: MdsMtlsConfig \u001b[38;5;241m=\u001b[39m MdsMtlsConfig()):\n\u001b[1;32m    102\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Determines if mTLS should be used for the metadata server.\"\"\"\u001b[39;00m\n\u001b[0;32m--> 103\u001b[0m     mode \u001b[38;5;241m=\u001b[39m \u001b[43m_parse_mds_mode\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    104\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m mode \u001b[38;5;241m==\u001b[39m MdsMtlsMode\u001b[38;5;241m.\u001b[39mSTRICT:\n\u001b[1;32m    105\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m _certs_exist(mds_mtls_config):\n",
      "File \u001b[0;32m/opt/conda/lib/python3.10/site-packages/google/auth/compute_engine/_mtls.py:91\u001b[0m, in \u001b[0;36m_parse_mds_mode\u001b[0;34m()\u001b[0m\n\u001b[1;32m     88\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_parse_mds_mode\u001b[39m():\n\u001b[1;32m     89\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Parses the GCE_METADATA_MTLS_MODE environment variable.\"\"\"\u001b[39;00m\n\u001b[1;32m     90\u001b[0m     mode_str \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\n\u001b[0;32m---> 91\u001b[0m         \u001b[43menvironment_vars\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mGCE_METADATA_MTLS_MODE\u001b[49m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdefault\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m     92\u001b[0m     )\u001b[38;5;241m.\u001b[39mlower()\n\u001b[1;32m     93\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m     94\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m MdsMtlsMode(mode_str)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'google.auth.environment_vars' has no attribute 'GCE_METADATA_MTLS_MODE'"
     ]
    }
   ],
   "source": [
    "sheet_music_pdf_uri = \"gs://github-repo/use-cases/sheet-music/SebbenCrudele.pdf\"\n",
    "output_file_name = \"SebbenCrudele.pdf\"\n",
    "\n",
    "sheet_music_extraction_prompt = \"\"\"The following document is a piece of sheet music. Your task is to output structured metadata about the piece of music in the document. Correct any mistakes that are in the document and fill in missing information when not present in the document.\n",
    "\n",
    "Output the data in the following JSON format:\n",
    "\n",
    "{\n",
    "    \"/Title\": \"Title of the piece\",\n",
    "    \"/Author\": \"Composer(s) of the piece\",\n",
    "    \"/Subject\": \"Music Genre(s) in a comma separated list\",\n",
    "}\n",
    "\n",
    "\"\"\"\n",
    "# Load file directly from Google Cloud Storage\n",
    "file_part = Part.from_uri(\n",
    "    file_uri=sheet_music_pdf_uri,\n",
    "    mime_type=\"application/pdf\",\n",
    ")\n",
    "\n",
    "temp_config = config.model_copy()\n",
    "\n",
    "# Send to Gemini\n",
    "response = client.models.generate_content(\n",
    "    model=MODEL_ID,\n",
    "    contents=[sheet_music_extraction_prompt, file_part],\n",
    "    config=temp_config,\n",
    ")\n",
    "\n",
    "raw_text = response.text.strip()\n",
    "\n",
    "start = raw_text.find('{')\n",
    "end = raw_text.find('}', start) + 1\n",
    "valid_json_string = raw_text[start:end]\n",
    "\n",
    "# Display the clean JSON before parsing\n",
    "display(Markdown(\"```json\\n\" + valid_json_string + \"\\n```\"))\n",
    "\n",
    "# Now, load the cleaned string into a dictionary\n",
    "new_metadata = json.loads(valid_json_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8e997cb6affc"
   },
   "source": [
    "Next, we'll download the PDF from the GCS Bucket and edit the metadata using the [`PyPDF2`](https://pypdf2.readthedocs.io/en/3.x/) library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "879f827c537a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Copying gs://github-repo/use-cases/sheet-music/SebbenCrudele.pdf to file://SebbenCrudele.pdf\n",
      "  Completed files 1/1 | 586.7kiB/586.7kiB                                      \n",
      "\n",
      "Average throughput: 276.5MiB/s\n"
     ]
    }
   ],
   "source": [
    "! gcloud storage cp {sheet_music_pdf_uri} {output_file_name}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "e81759999d78"
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'new_metadata' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[10], line 20\u001b[0m\n\u001b[1;32m     16\u001b[0m         \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(file_path, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mwb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m out_file:\n\u001b[1;32m     17\u001b[0m             pdf_writer\u001b[38;5;241m.\u001b[39mwrite(out_file)\n\u001b[0;32m---> 20\u001b[0m edit_pdf_metadata(output_file_name, \u001b[43mnew_metadata\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'new_metadata' is not defined"
     ]
    }
   ],
   "source": [
    "def edit_pdf_metadata(file_path: str, new_metadata: dict) -> None:\n",
    "    \"\"\"Edits metadata of a PDF file.\n",
    "\n",
    "    Args:\n",
    "        file_path (str): Path to the PDF file.\n",
    "        new_metadata (dict): Dictionary containing the new metadata fields and values.\n",
    "            Example: {'/Author': 'John Doe', '/Title': 'My Report'}\n",
    "    \"\"\"\n",
    "    with open(file_path, \"rb\") as pdf_file:\n",
    "        pdf_reader = PyPDF2.PdfReader(pdf_file)\n",
    "        pdf_writer = PyPDF2.PdfWriter()\n",
    "\n",
    "        pdf_writer.clone_reader_document_root(pdf_reader)\n",
    "        pdf_writer.add_metadata(new_metadata)\n",
    "\n",
    "        with open(file_path, \"wb\") as out_file:\n",
    "            pdf_writer.write(out_file)\n",
    "\n",
    "\n",
    "edit_pdf_metadata(output_file_name, new_metadata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "jtbQo-df1TTu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'/Producer': 'macOS Version 14.5 (Build 23F79) Quartz PDFContext', '/Creator': 'PDFium', '/CreationDate': \"D:20240624193407Z00'00'\", '/ModDate': \"D:20240624193407Z00'00'\"}\n"
     ]
    }
   ],
   "source": [
    "pdf_reader = PyPDF2.PdfReader(output_file_name)\n",
    "print(pdf_reader.metadata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "sheet_music.ipynb",
   "toc_visible": true
  },
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m137",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m137"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local) (Local)",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
