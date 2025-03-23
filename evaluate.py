from transformers import T5Tokenizer, T5ForConditionalGeneration
from rouge_score import rouge_scorer

# Load the trained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('./grass_gis_chatbot_model')
tokenizer = T5Tokenizer.from_pretrained('./grass_gis_chatbot_model')

# Test set
test_set = [
    {"input": "gis: How do I calculate the slope for a raster?", "output": "Command: r.slope.aspect\nExample: r.slope.aspect elevation=elevation_map slope=slope_map"},
    {"input": "gis: What command do I use for raster algebra?", "output": "Command: r.mapcalc\nExample: r.mapcalc 'new_raster = raster1 + raster2'"},
    {"input": "gis: How do I create a vector map from a raster?", "output": "Command: r.to.vect\nExample: r.to.vect input=raster_map output=vector_map type=area"},
    {"input": "gis: How do I display a raster map?", "output": "Command: d.rast\nExample: d.rast map=raster_map"},
    {"input": "gis: How can I list all available raster maps?", "output": "Command: g.list\nExample: g.list type=raster"},
    {"input": "gis: How do I set the computational region to match a specific raster map?", "output": "Command: g.region\nExample: g.region raster=elevation_map"},
    {"input": "gis: How can I import a GeoTIFF file into GRASS GIS?", "output": "Command: r.import\nExample: r.import input=path/to/file.tif output=raster_map"},
    {"input": "gis: How do I export a raster map to a GeoTIFF file?", "output": "Command: r.out.gdal\nExample: r.out.gdal input=raster_map output=output_file.tif format=GTiff"},
    {"input": "gis: How can I reproject a vector map to a different coordinate system?", "output": "Command: v.proj\nExample: v.proj input=vector_map location=target_location"},
    {"input": "gis: How do I calculate the area of each polygon in a vector map?", "output": "Command: v.to.db\nExample: v.to.db map=vector_map option=area columns=area"},
    {"input": "gis: How can I buffer vector features by a specific distance?", "output": "Command: v.buffer\nExample: v.buffer input=vector_map output=buffered_map distance=100"},
    {"input": "gis: How do I clip a vector map using another vector map as a mask?", "output": "Command: v.overlay\nExample: v.overlay ainput=vector_map binput=mask_map operator=and output=clipped_map"},
    {"input": "gis: How can I dissolve boundaries between adjacent polygons with the same attribute?", "output": "Command: v.dissolve\nExample: v.dissolve input=vector_map column=attribute_column output=dissolved_map"},
    {"input": "gis: How do I remove small areas (islands) from a vector map?", "output": "Command: v.clean\nExample: v.clean input=vector_map output=cleaned_map tool=rmarea threshold=1000"},
    {"input": "gis: How can I simplify the geometry of vector features?", "output": "Command: v.generalize\nExample: v.generalize input=vector_map output=simplified_map method=douglas threshold=10"},
    {"input": "gis: How do I convert a vector map to a raster map?", "output": "Command: v.to.rast\nExample: v.to.rast input=vector_map output=raster_map use=attr attribute_column=value"},
    {"input": "gis: How can I patch multiple raster maps into a single raster map?", "output": "Command: r.patch\nExample: r.patch input=map1,map2,map3 output=patched_map"},
    {"input": "gis: How do I fill null (no-data) cells in a raster map?", "output": "Command: r.fillnulls\nExample: r.fillnulls input=raster_map output=filled_map"},
    {"input": "gis: How can I calculate statistics for a raster map?", "output": "Command: r.univar\nExample: r.univar map=raster_map"},
    {"input": "gis: How do I resample a raster map to a different resolution?", "output": "Command: r.resamp.interp\nExample: r.resamp.interp input=raster_map output=resampled_map method=bilinear"},
    {"input": "gis: How can I extract contour lines from a raster elevation map?", "output": "Command: r.contour\nExample: r.contour input=elevation_map output=contours step=10"}
]

# Function to evaluate ROUGE score
def evaluate_rouge(test_set):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    rouge_scores = {"rouge1": [], "rouge2": [], "rougeL": []}

    for item in test_set:
        input_text = item["input"]
        expected_output = item["output"]

        input_ids = tokenizer(input_text, return_tensors='pt').input_ids
        output_ids = model.generate(input_ids, max_length=256, num_beams=5, early_stopping=True)
        generated_output = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

        score = scorer.score(expected_output, generated_output)

        rouge_scores["rouge1"].append(score["rouge1"].fmeasure)
        rouge_scores["rouge2"].append(score["rouge2"].fmeasure)
        rouge_scores["rougeL"].append(score["rougeL"].fmeasure)

    avg_rouge1 = sum(rouge_scores["rouge1"]) / len(rouge_scores["rouge1"])
    avg_rouge2 = sum(rouge_scores["rouge2"]) / len(rouge_scores["rouge2"])
    avg_rougeL = sum(rouge_scores["rougeL"]) / len(rouge_scores["rougeL"])

    print(f"Average ROUGE-1: {avg_rouge1:.4f}")
    print(f"Average ROUGE-2: {avg_rouge2:.4f}")
    print(f"Average ROUGE-L: {avg_rougeL:.4f}")

evaluate_rouge(test_set)
