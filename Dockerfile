FROM wlserver1/ytupload:latest
ADD ./ /
RUN pip3 install cloudinary
RUN python3 views.py
RUN python -m pip install --upgrade gtts
RUN python -m pip install --upgrade gtts-token