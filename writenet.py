    def forward(self, template, detection, weight=None):
        if weight==None:
            N = template.size(0)
            template_feature = self.featureExtract(template)
            detection_feature = self.featureExtract(detection)

            kernel_score = self.conv_cls1(template_feature).view(N, 2 * self.anchor_num, 256, 4, 4)
            kernel_regression = self.conv_r1(template_feature).view(N, 4 * self.anchor_num, 256, 4, 4)
            conv_score = self.conv_cls2(detection_feature)
            conv_regression = self.conv_r2(detection_feature)

            conv_scores = conv_score.reshape(1, -1, self.score_displacement + 4, self.score_displacement + 4)
            score_filters = kernel_score.reshape(-1, 256, 4, 4)
            pred_score = F.conv2d(conv_scores, score_filters, groups=N).reshape(N, 10, self.score_displacement + 1,
                                                                                self.score_displacement + 1)

            conv_reg = conv_regression.reshape(1, -1, self.score_displacement + 4, self.score_displacement + 4)
            reg_filters = kernel_regression.reshape(-1, 256, 4, 4)
            pred_regression = self.regress_adjust(
                F.conv2d(conv_reg, reg_filters, groups=N).reshape(N, 20, self.score_displacement + 1,
                                                                  self.score_displacement + 1))
        else:
            # x=self.extract(x)
            N = template.size(0)
            template_feature = self.extract(template)
            detection_feature = self.extract(detection)

            kernel_score = conv2d(template_feature, weight['conv_cls1.weight'], weight['conv_cls1.bias'], stride=1, padding=0).view(N, 2 * self.anchor_num, 256, 4, 4)
            kernel_regression = conv2d(template_feature, weight['conv_r1.weight'], weight['conv_r1.bias'] stride=1, padding=0).view(N, 4 * self.anchor_num, 256, 4, 4)
            conv_score = conv2d(detection_feature, weight['conv_cls2.weight'], weight['conv_cls2.bias'])
            conv_regression = conv2d(detection_feature, weight['conv_r2.weight'], weight['conv_r2.bias'])

            conv_scores = conv_score.reshape(1, -1, self.score_displacement + 4, self.score_displacement + 4)
            score_filters = kernel_score.reshape(-1, 256, 4, 4)
            pred_score = F.conv2d(conv_scores, score_filters, groups=N).reshape(N, 10, self.score_displacement + 1,
                                                                                self.score_displacement + 1)

            conv_reg = conv_regression.reshape(1, -1, self.score_displacement + 4, self.score_displacement + 4)
            reg_filters = kernel_regression.reshape(-1, 256, 4, 4)
            pred_regression = self.regress_adjust(
                F.conv2d(conv_reg, weight['regress_adjust.weight'],weight['regress_adjust.bias'], groups=N).reshape(N, 20, self.score_displacement + 1,
                                                                  self.score_displacement + 1))
