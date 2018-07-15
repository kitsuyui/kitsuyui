FROM alpine
ADD x.sh .
ADD y.sh .
RUN \
test "$(./x.sh)" = 'Hello' && \
test "$(./y.sh)" = ''
